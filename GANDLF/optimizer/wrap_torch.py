from torch.optim import  SGD, ASGD, Rprop, Adam, AdamW, SparseAdam, Adamax, Adadelta, Adagrad, RMSprop, LBFGS

def sgd(parameters, model_parameters):
    # pick defaults
    if not ("momentum" in parameters["optimizer"]):
        parameters["optimizer"]["momentum"] = 0.9
    if not ("weight_decay" in parameters["optimizer"]):
        parameters["optimizer"]["weight_decay"] = 0
    if not ("dampening" in parameters["optimizer"]):
        parameters["optimizer"]["dampening"] = 0
    if not ("nesterov" in parameters["optimizer"]):
        parameters["optimizer"]["nesterov"] = False
    return SGD(model_parameters, lr=parameters["learning_rate"], momentum=parameters["optimizer"]["momentum"], weight_decay=parameters["optimizer"]["weight_decay"], dampening=parameters["optimizer"]["dampening"],nesterov=parameters["optimizer"]["nesterov"])

def asgd(parameters, model_parameters):
    # pick defaults
    if not ("lambd" in parameters["optimizer"]):
        parameters["optimizer"]["lambd"] = 1e-4
    if not ("alpha" in parameters["optimizer"]):
        parameters["optimizer"]["alpha"] = 0.75
    if not ("t0" in parameters["optimizer"]):
        parameters["optimizer"]["t0"] = 1e6
    if not ("weight_decay" in parameters["optimizer"]):
        parameters["optimizer"]["weight_decay"] = 0
    return ASGD(model_parameters, lr=parameters["learning_rate"], alpha=parameters["optimizer"]["alpha"], t0=parameters["optimizer"]["t0"], lambd=parameters["optimizer"]["lambd"], weight_decay=parameters["optimizer"]["weight_decay"])

def adam(parameters, model_parameters):
    # pick defaults
    if not ("betas" in parameters["optimizer"]):
        parameters["optimizer"]["betas"] = (0.9, 0.999)
    if not ("weight_decay" in parameters["optimizer"]):
        parameters["optimizer"]["weight_decay"] = 0.00005
    if not ("eps" in parameters["optimizer"]):
        parameters["optimizer"]["eps"] = 1e-8
    if not ("amsgrad" in parameters["optimizer"]):
        parameters["optimizer"]["amsgrad"] = False
    return Adam(
            model_parameters, lr=parameters["learning_rate"], betas=parameters["optimizer"]["betas"], weight_decay=parameters["optimizer"]["weight_decay"], eps=parameters["optimizer"]["eps"], amsgrad=parameters["optimizer"]["amsgrad"])
