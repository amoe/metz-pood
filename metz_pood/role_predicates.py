from metz_pood.test_utility import responds_to

def is_diameterizable(obj):
    return responds_to(obj, 'width')

def assert_is_bicycle(obj):
    assert [1] == [1,2]
#    assert 2 +2 == 5
    # c = (
    #     responds_to(obj, 'default_tire_size'),
    #     responds_to(obj, 'default_chain'),
    #     responds_to(obj, 'chain'),
    #     responds_to(obj, 'size'),
    #     responds_to(obj, 'tire_size'),
    #     responds_to(obj, 'spares')
    # )

