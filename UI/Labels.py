Labels = {}

def Add(newlabels):
    Labels.update(newlabels)

def Label(label):
    return Labels.get(label, label)
