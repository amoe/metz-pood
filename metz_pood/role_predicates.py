from metz_pood.test_utility import responds_to

def is_diameterizable(obj):
    return responds_to(obj, 'width')
