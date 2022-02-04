class Optimizer():
    """Optimize a given function for the provided, parameter space

    Args:
        | target_value (float):
                Value the optimizer is trying to achieve by using check_method
        | run_method (function):
                Function to call with an updated param_list for the next iteration
        | check_method (function):
                Function to call to evaluate on whether or not progress has been made
        | param_dict (dictionary):
                Keys represent variables used in the run method to produce a different outcome
        | opt_param_list (list of dicts):
                List of dictionaries, with each key representing a parameter that may be changed by the optimizer; these
                keys should be present in param_dict already
        | proxmity (float):
                """

    def __init__(self, target_value, run_method, check_method, param_dict, opt_param_list, proximity=0.1):
        pass

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass