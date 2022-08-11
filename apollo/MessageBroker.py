import time
from typing import List
from logging import Logger
from threading import Thread
from modules.common.proto.header_pb2 import Header
from modules.perception.proto.perception_obstacle_pb2 import PerceptionObstacles
from apollo.utils import localization_to_obstacle
from apollo.CyberBridge import Channel, Topics
from utils import get_logger
from config import PERCEPTION_FREQUENCY
from apollo.ApolloRunner import ApolloRunner


class MessageBroker:
    """
    Class to represent MessageBroker

    Attributes:
    runners: List[ApolloRunners]
        list of running Apollo instances
    spinning: bool
        whether the message broker should forward localization as obstacle
    logger: Logger
        logging the status of the message broker
    t: Thread
        background thread to forward data
    """
    runners: List[ApolloRunner]
    spinning: bool
    logger: Logger
    t: Thread

    def __init__(self, runners: List[ApolloRunner]) -> None:
        """
        Constructs all the attributes for MessageBroker

        Parameters:
            runners: List[ApolloRunner]
                list of running Apollo instances
        """
        self.runners = runners
        self.spinning = False
        self.logger = get_logger('MessageBroker')

    def broadcast(self, channel: Channel, data: bytes):
        """
        Sends data to every instance

        Parameters:
            channel: Channel
                channel to send data to
            data: bytes
                data to be sent
        """
        for runner in self.runners:
            runner.container.bridge.publish(channel, data)

    def _spin(self):
        """
        Helper function to start forwarding localization
        """
        header_sequence_num = 0
        while self.spinning:
            # retrieve localization of running instances
            locations = dict()
            for runner in self.runners:
                if runner.is_running:
                    loc = runner.localization
                    if loc and loc.header.module_name == 'SimControl':
                        locations[runner.nid] = runner.localization

            # convert localization into obstacles
            obs = dict()
            for k in locations:
                obs[k] = localization_to_obstacle(k, locations[k])

            # publish obstacle to all running instances
            for runner in self.runners:
                if runner.is_running:
                    perception_obs = [obs[x]
                                      for x in obs if x != runner.nid]
                    header = Header(
                        timestamp_sec=time.time(),
                        module_name='MAGGIE',
                        sequence_num=header_sequence_num
                    )
                    bag = PerceptionObstacles(
                        header=header,
                        perception_obstacle=perception_obs,
                    )
                    runner.container.bridge.publish(
                        Topics.Obstacles, bag.SerializeToString()
                    )
            header_sequence_num += 1
            time.sleep(1/PERCEPTION_FREQUENCY)

    def spin(self):
        """
        Starts to forward localization
        """
        self.logger.debug('Starting to spin')
        if self.spinning:
            return
        self.t = Thread(target=self._spin)
        self.spinning = True
        self.t.start()

    def stop(self):
        """
        Stops forwarding localization
        """
        self.logger.debug('Stopping')
        if not self.spinning:
            return
        self.spinning = False
        self.t.join()
