"""CoronaVirus LookUp
Syntax: .corona <country>"""

from covid import Covid

from userbot.utils import lightning_cmd


@borg.on(lightning_cmd(pattern="corona (.*)"))
async def _(event):

    covid = Covid()

    data = covid.get_data()

    country = event.pattern_match.group(1)

    country_data = get_country_data(country, data)

    output_text = "".join(
        "`{}`: `{}`\n".format(str(name), str(value))
        for name, value in country_data.items()
    )


    await event.edit(
        "**CoronaVirus Info in {}**:\n\n{}".format(country.capitalize(), output_text)
    )


def get_country_data(country, world):

    for country_data in world:

        if country_data["country"].lower() == country.lower():

            return country_data

    return {"Status": "No information yet about this country!"}
