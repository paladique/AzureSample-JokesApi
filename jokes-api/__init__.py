import logging
import random
import azure.functions as func

def getRandomJoke(list):
    return list[random.randint(0,len(list)-1)]

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # jokes from here: https://www.rd.com/jokes/computer/
    tech_jokes = ['Don\'t use "beef stew" as a computer password. It\'s not stroganoff.',
    'Why are iPhone chargers not called Apple Juice?!',
    'Q. Why did the PowerPoint Presentation cross the road? A. To get to the other slide.',
    'We\'ll we\'ll we\'ll...if it isn\'t autocorrect.' ]

    # jokes from here: https://bestlifeonline.com/funny-short-jokes/
    silly_jokes = ['How do you throw a space party? You planet!',
    'Why don\'t scientists trust atoms? Because they make up everything!',
    'Q. Where are average things manufactured? A. The satisfactory.',
    'Why doesn\'t the sun go to college? Because it has a million degrees!']

    random_jokes = tech_jokes + silly_jokes
    

    joke = req.params.get('joke')

    if not joke:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            joke = req_body.get('jokes')

    if joke == 'tech' or joke =='silly':
        
        rtn_joke = getRandomJoke(tech_jokes if joke =='tech' else silly_jokes)
        return func.HttpResponse(
            rtn_joke, 
            status_code=200
            )
    else:
        rtn_joke = getRandomJoke(random_jokes)
        return func.HttpResponse(
            rtn_joke,
            status_code=200
        )

