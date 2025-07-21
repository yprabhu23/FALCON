import os
import sys
import time

import numpy as np
import argparse
import yaml

sys.path.append("../")
sys.path.append("./sim2real")

import pinocchio as pin
from sim2real.rl_policy.dec_loco.dec_loco import DecLocomotionPolicy

from termcolor import colored
from sim2real.utils.arm_ik.robot_arm_ik_g1_23dof import G1_29_ArmIK_NoWrists


g1_config = "config/g1/g1_29dof.yaml"

with open(g1_config) as file:
        config = yaml.safe_load(file)

upper_body_controller = G1_29_ArmIK_NoWrists(
                Unit_Test=False, Visualization=True, robot_config=config
                )