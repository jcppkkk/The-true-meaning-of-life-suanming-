# coding:utf-8
from sanic import Sanic, response
from sanic.response import text

from get_life import YEAR_MAP, MONTH_MAP, DAY_MAP, HOUR, LIFE_MAP

app = Sanic(__name__)


@app.route("/")
async def home(request):
    return text(
        "稱骨算命法，相傳是唐朝週易大師袁天罡先生所創，其法將人的生辰八字，即出生的農歷年月日時計算相應的“骨重”，然後根據“稱骨”的總值來進行算命。(古代的重量單位：1斤=10兩，1兩=10錢)"
    )


@app.route("/suan_ming", methods=["POST"])
async def post_data(request):
    year = request.args.get("year")
    month = request.args.get("month")
    day = request.args.get("day")
    hour = request.args.get("hour")
    try:
        score = YEAR_MAP[year] + MONTH_MAP[month] + DAY_MAP[day] + HOUR[hour]
        life_language = LIFE_MAP[str(int(score))]
        weight_list = str(score).split(".")
        life_weight = weight_list[0] + "兩" + weight_list[1] + "錢"
    except:
        life_language, life_weight = "我命由我不由天！", "0"
    return response.json({"life_language": life_language, "life_weight": life_weight})


app.run(host="0.0.0.0", port=8000, debug=True)
