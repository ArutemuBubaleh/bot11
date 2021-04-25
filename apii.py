from flask import Flask
from flask_restful import Api, Resource, reqparse
import random

app = Flask(__name__)
api = Api(app)
ai_quotes = [
    {
        "name": "Морячок",
        "track": "https://www.youtube.com/watch?v=RHpftBEUC5Q",
        "clip": "-отсутствует-",
        "lyrics":
            'А на море ветер свищет\n;'
            'Моряка никто не ищет\n'
            'Морячок наверно затонул\n'
            'И на дне страной забытой\n'
            'Он лежит волной убитый\n'
            'И к морскому дну навек прильнул\n'

            'Лишь у ней сердечко стонет:\n'
            '"Как же так? Он не утонет.\n'
            'Не оставит здесь одну меня.\n'
            'А моряк давно женился,\n'
            'Потолстел и обленился\n'
            'И не ходит в море - дом семья"\n'

            'Лишь одна о нём скучает\n'
            'Корабли в порту встречает\n'
            'И кричит волнам: " А как же я!?"\n'
            'Но волна о пристань грянет\n'
            'И сынок за руку тянет\n'
            'Погремушкой глупою звеня\n'
    },
    {
        "name": "Вампир",
        "track": "https://www.youtube.com/watch?v=9kX7VQm5cmU",
        "clip": "https://www.youtube.com/watch?v=Mz0NqSa_wVM",
        "lyrics":
            'Тут хуячу на свидание\n'
            'Прохожу ларек и здание\n'
            'Захожу во двор сквозь арку,\n'
            'Тут заметил иномарку -\n'
            'Бумер, бля, крутая тачка,\n'
            'за рулем такая пачка!\n'
            'Шефа ждет, видать, братуха,\n'
            'На меня глазеет сухо\n'

            'Наступив в говна, бля, кучу\n'
            'Захожу в подъезд вонючий\n'
            'В жопе, бля, светлей наверное,\n'
            'И воняет также скверно\n'
            'У меня в руках конфетки\n'
            'И букетик роз для Светки\n'
            'Ждет меня моя отрада,\n'
            'Любит, блядь, такого гада!\n'

            'Ну а хули, я же тоже,\n'
            'Хоть и жизни прошлась по роже.\n'
            'Проходя огонь и трубы,\n'
            'Потерял друзей и зубы.\n'
            'Был в тузах, потом - валетом.\n'
            'Впрочем, речь сейчас не об этом.\n'
            'На этаж заполз к Светуле, тут, хуяк, стрельба, блядь, пули!!!\n'

            'Дверь, косяк, стекло, кровища.\n'
            'Всё летит мне, бля, в еблище.\n'
            'Озаряя чудным светом,\n'
            'выбегают два брюнета\n'
            'и по мне хуячат дружно,\n'
            'Я лежу, мне выпить нужно.\n'
            'Весь в дерьме, букетик смятый,\n'
            'Слышу крик: "Спасибо, снято!"\n'

            'Мужики снуют, бабёнки -\n'
            'Я ебал такие съемки!!!\n'
            'Светка мне, пизда, моргает:\n'
            '"А у нас кино снимают!"\n'
            '"Мент-вампир" кино назвали,\n'
            'и меня на пробы звали...\n'
            'ЗВАЛИ!!! Суку...',
    },
    {
        "name": "Кризис",
        "track": "https://www.youtube.com/watch?v=EjQSAuQTgHg",
        "clip": "https://www.youtube.com/watch?v=Mz0NqSa_wVM",
        "lyrics":
            'Листья жмутся к земле поближе,\n'
            'Потому что боятся ночи\n'
            'Я и сам эти тучи вижу.\n'
            'И ты знаешь, мне страшно очень.\n'

            'С неба капли, кап-кап- и лужа\n'
            'А за лужей другая тут же.\n'
            'И чего этим лужам нужно,\n'
            'Все равно уж не будет хуже.\n'

            'Кризис грянул и нет спасенья,\n'
            'Нет спасенья, хоть прыгай с кручи…\n'
            'Все твои щас и к месту рвенья, глянь какие подходят тучи.\n'
            'Глянь, какая сверкнула сабля, сколько сразу голов срубила,\n'
            'А за саблей, упала капля, кровь барыги с асфальта смыла.\n'

            'Вон другая сверкнула туча,\n'
            'Покатилась башка банкира.\n'
            'Ничего быть нее может хуже\n'
            'Ролик банка пропал с эфира.\n'

            'Ты к попу не ходи, уж поздно\n'
            'Он конечно проявит ласку,\n'
            'Но мольбу не услышат звезды.\n'
            'Рано брат ты поверил в сказку'
    }]


class Quote(Resource):
    def get(self, id=0):
        if id == 0:
            return random.choice(ai_quotes), 200
        for quote in ai_quotes:
            if (quote["name"] == id):
                return quote, 200
        return "Quote not found", 404

    def post(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("track")
        parser.add_argument("clip")
        parser.add_argument("lyrics")
        params = parser.parse_args()
        for quote in ai_quotes:
            if (id == quote["name"]):
                return f"Quote with id {id} already exists", 400
        quote = {
            "name": int(id),
            "track": params["track"],
            "clip": params["clip"],
            "lyrics": params["lyrics"]
        }
        ai_quotes.append(quote)
        return quote, 201

    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("track")
        parser.add_argument("clip")
        params = parser.parse_args()
        for quote in ai_quotes:
            if (id == quote["name"]):
                quote["track"] = params["track"]
                quote["clip"] = params["clip"]
                return quote, 200

        quote = {
            "name": id,
            "track": params["track"],
            "clip": params["clip"]
        }

        ai_quotes.append(quote)
        return quote, 201

    def delete(self, id):
        global ai_quotes
        ai_quotes = [qoute for qoute in ai_quotes if qoute["name"] != id]
        return f"Quote with id {id} is deleted.", 200


api.add_resource(Quote, "/ai-quotes", "/ai-quotes/", "/ai-quotes/<int:id>")
if __name__ == '__main__':
    app.run(debug=True)
