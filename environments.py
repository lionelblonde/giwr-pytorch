# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> MuJoCo environments.

MUJOCO_ROBOTS = [
    'InvertedPendulum',
    'InvertedDoublePendulum',
    'Reacher',
    'Hopper',
    'HalfCheetah',
    'Walker2d',
    'Ant',
    'Humanoid',
]

MUJOCO_ENVS = ["{}-v2".format(name) for name in MUJOCO_ROBOTS]
MUJOCO_ENVS.extend(["{}-v3".format(name) for name in MUJOCO_ROBOTS])

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> D4RL environments.

# Note, we here consider every environment of the benchmark except 'carla-town-full-v0',
# since a) it is too complex for this work, and b) no score info had been provided with the code.

REF_MIN_SCORE = {
    'maze2d-open-v0': 0.01,
    'maze2d-umaze-v1': 23.85,
    'maze2d-medium-v1': 13.13,
    'maze2d-large-v1': 6.7,
    'maze2d-open-dense-v0': 11.17817,
    'maze2d-umaze-dense-v1': 68.537689,
    'maze2d-medium-dense-v1': 44.264742,
    'maze2d-large-dense-v1': 30.569041,
    'minigrid-fourrooms-v0': 0.01442,
    'minigrid-fourrooms-random-v0': 0.01442,
    'pen-human-v0': 96.262799,
    'pen-cloned-v0': 96.262799,
    'pen-expert-v0': 96.262799,
    'hammer-human-v0': -274.856578,
    'hammer-cloned-v0': -274.856578,
    'hammer-expert-v0': -274.856578,
    'relocate-human-v0': -6.425911,
    'relocate-cloned-v0': -6.425911,
    'relocate-expert-v0': -6.425911,
    'door-human-v0': -56.512833,
    'door-cloned-v0': -56.512833,
    'door-expert-v0': -56.512833,
    'halfcheetah-random-v0': -280.178953,
    'halfcheetah-medium-v0': -280.178953,
    'halfcheetah-expert-v0': -280.178953,
    'halfcheetah-medium-replay-v0': -280.178953,
    'halfcheetah-medium-expert-v0': -280.178953,
    'walker2d-random-v0': 1.629008,
    'walker2d-medium-v0': 1.629008,
    'walker2d-expert-v0': 1.629008,
    'walker2d-medium-replay-v0': 1.629008,
    'walker2d-medium-expert-v0': 1.629008,
    'hopper-random-v0': -20.272305,
    'hopper-medium-v0': -20.272305,
    'hopper-expert-v0': -20.272305,
    'hopper-medium-replay-v0': -20.272305,
    'hopper-medium-expert-v0': -20.272305,
    'antmaze-umaze-v0': 0.0,
    'antmaze-umaze-diverse-v0': 0.0,
    'antmaze-medium-play-v0': 0.0,
    'antmaze-medium-diverse-v0': 0.0,
    'antmaze-large-play-v0': 0.0,
    'antmaze-large-diverse-v0': 0.0,
    'kitchen-complete-v0': 0.0,
    'kitchen-partial-v0': 0.0,
    'kitchen-mixed-v0': 0.0,
    'flow-ring-random-v0': -165.22,
    'flow-ring-controller-v0': -165.22,
    'flow-merge-random-v0': 118.67993,
    'flow-merge-controller-v0': 118.67993,
    'carla-lane-v0': -0.8503839912088142,
    'carla-town-v0': -122.228455,
}

REF_MAX_SCORE = {
    'maze2d-open-v0': 20.66,
    'maze2d-umaze-v1': 161.86,
    'maze2d-medium-v1': 277.39,
    'maze2d-large-v1': 273.99,
    'maze2d-open-dense-v0': 27.166538620695782,
    'maze2d-umaze-dense-v1': 193.66285642381482,
    'maze2d-medium-dense-v1': 297.4552547777125,
    'maze2d-large-dense-v1': 303.4857382709002,
    'minigrid-fourrooms-v0': 2.89685,
    'minigrid-fourrooms-random-v0': 2.89685,
    'pen-human-v0': 3076.8331017826877,
    'pen-cloned-v0': 3076.8331017826877,
    'pen-expert-v0': 3076.8331017826877,
    'hammer-human-v0': 12794.134825156867,
    'hammer-cloned-v0': 12794.134825156867,
    'hammer-expert-v0': 12794.134825156867,
    'relocate-human-v0': 4233.877797728884,
    'relocate-cloned-v0': 4233.877797728884,
    'relocate-expert-v0': 4233.877797728884,
    'door-human-v0': 2880.5693087298737,
    'door-cloned-v0': 2880.5693087298737,
    'door-expert-v0': 2880.5693087298737,
    'halfcheetah-random-v0': 12135.0,
    'halfcheetah-medium-v0': 12135.0,
    'halfcheetah-expert-v0': 12135.0,
    'halfcheetah-medium-replay-v0': 12135.0,
    'halfcheetah-medium-expert-v0': 12135.0,
    'walker2d-random-v0': 4592.3,
    'walker2d-medium-v0': 4592.3,
    'walker2d-expert-v0': 4592.3,
    'walker2d-medium-replay-v0': 4592.3,
    'walker2d-medium-expert-v0': 4592.3,
    'hopper-random-v0': 3234.3,
    'hopper-medium-v0': 3234.3,
    'hopper-expert-v0': 3234.3,
    'hopper-medium-replay-v0': 3234.3,
    'hopper-medium-expert-v0': 3234.3,
    'antmaze-umaze-v0': 1.0,
    'antmaze-umaze-diverse-v0': 1.0,
    'antmaze-medium-play-v0': 1.0,
    'antmaze-medium-diverse-v0': 1.0,
    'antmaze-large-play-v0': 1.0,
    'antmaze-large-diverse-v0': 1.0,
    'kitchen-complete-v0': 4.0,
    'kitchen-partial-v0': 4.0,
    'kitchen-mixed-v0': 4.0,
    'flow-ring-random-v0': 24.42,
    'flow-ring-controller-v0': 24.42,
    'flow-merge-random-v0': 330.03179,
    'flow-merge-controller-v0': 330.03179,
    'carla-lane-v0': 1023.5784385429523,
    'carla-town-v0': -64.62967840318221,
}

assert list(REF_MIN_SCORE.keys()) == list(REF_MAX_SCORE.keys())
D4RL_ENVS = list(REF_MIN_SCORE.keys())

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Aggregate the environments

BENCHMARKS = {
    'mujoco': MUJOCO_ENVS,
    'd4rl': D4RL_ENVS,
}
