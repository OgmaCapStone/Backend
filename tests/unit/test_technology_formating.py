from app.utils.technologies_formating import technologies_formating
technologies = [

    ["id","tech","tech image","tech summary"]
]

def test_should_pass():
    assert technologies_formating(technologies) == {"response": [{"name": technologies[0][1], "image": technologies[0][2], "summary": technologies[0][3]}]}

def test_should_not_pass():
    assert technologies_formating(technologies) != {"response": [{"name": technologies[0][0], "image": technologies[0][3], "summary": technologies[0][1]}]}