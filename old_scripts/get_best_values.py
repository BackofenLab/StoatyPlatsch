import numpy

def get_best_values(spec, output):
    # model_params = {
    #     'GaussianModel':   ['amplitude', 'sigma'],
    #     'LorentzianModel': ['amplitude', 'sigma'],
    #     'VoigtModel':      ['amplitude', 'sigma', 'gamma'],
    #     'SkewedGaussianModel': ['amplitude', 'sigma', 'gamma'],
    #     'SkewedVoigtModel': ['amplitude', 'sigma', 'gamma'],
    #     'MoffatModel':  ['amplitude', 'sigma', 'beta'],
    #     'StudentsTModel': ['amplitude', 'sigma'],
    #     'BreitWignerModel': ['amplitude', 'sigma', 'q'],
    #     'DampedOscillatorModel': ['amplitude', 'sigma'],
    #     'DampedHarmonicOscillatorModel': ['amplitude', 'sigma', 'gamma'],
    #     'ExponentialGaussianModel': ['amplitude', 'sigma', 'gamma'],
    #     'DonaichModel': ['amplitude', 'sigma', 'gamma'],
    #     'StepModel': ['amplitude', 'sigma'],
    #     'RectangleModel': ['amplitude', 'sigma1', 'sigma2']
    # }
    best_values = output.best_values
    centeres = []
    sigma = []
    #print('center    model :  amplitude     sigma      gamma')
    for i, model in enumerate(spec['model']):
        prefix = f'm{i}_'
        #values = ', '.join(f'{best_values[prefix+param]:8.3f}' for param in model_params[model["type"]])
        #print(f'[{best_values[prefix+"center"]:3.3f}] {model["type"]:16}: {values}')
        centeres.append(numpy.floor(best_values[prefix + "center"]))
        sigma.append(best_values[prefix + "sigma"])
    return([centeres, sigma])