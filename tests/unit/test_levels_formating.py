from app.utils.levels_formating import levels_formating

levels = [
    ["junior"],
    ["junior_advanced"],
    ["mid"],
    ["mid_advanced"],
    ["senior"],
    ["senior_advanced"],
    ["legend"]
]

def test_should_pass():
    assert levels_formating(levels) == {"response": ["junior","junior_advanced","mid","mid_advanced","senior","senior_advanced","legend"]}

def test_should_not_pass():
    assert levels_formating(levels) != {"response": {"levels": ["junior","junior_advanced","mid","mid_advanced","senior","senior_advanced","legend"]}}