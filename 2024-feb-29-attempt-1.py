pre_pro = 0

def reward_function(params):
    global pre_pro
    # Read input parameters
    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    progress = params['progress']
    abs_steering = abs(params['steering_angle'])
    speed = params['speed']
    
    
    # Give a very low reward by default
    reward = 1e-3

    # Give a high reward if no wheels go off the track and
    # the agent is somewhere in between the track borders
    if all_wheels_on_track and (0.5*track_width - distance_from_center) >= 0.05:
        reward = 1.0 
    if abs_steering > 30 and speed > 2:
        reward -= 2
    if progress > pre_pro:
        reward += 1
        pre_pro = progress

    # Always return a float value
    return float(reward)
