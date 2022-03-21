import json

import numpy as np

import gradio as gr

CHOICES = ["foo", "bar", "baz"]
JSONOBJ = """{"items":{"item":[{"id": "0001","type": null,"is_good": false,"ppu": 0.55,"batters":{"batter":[{ "id": "1001", "type": "Regular" },{ "id": "1002", "type": "Chocolate" },{ "id": "1003", "type": "Blueberry" },{ "id": "1004", "type": "Devil's Food" }]},"topping":[{ "id": "5001", "type": "None" },{ "id": "5002", "type": "Glazed" },{ "id": "5005", "type": "Sugar" },{ "id": "5007", "type": "Powdered Sugar" },{ "id": "5006", "type": "Chocolate with Sprinkles" },{ "id": "5003", "type": "Chocolate" },{ "id": "5004", "type": "Maple" }]}]}}"""


def fn(
    text1,
    text2,
    num,
    slider1,
    slider2,
    single_checkbox,
    checkboxes,
    radio,
    dropdown,
    im1,
    im2,
    im3,
    im4,
    video,
    audio1,
    audio2,
    file,
    df1,
    df2,
):
    return (
        (text1 if single_checkbox else text2)
        + ", selected:"
        + ", ".join(checkboxes),  # Text
        {
            "positive": num / (num + slider1 + slider2),
            "negative": slider1 / (num + slider1 + slider2),
            "neutral": slider2 / (num + slider1 + slider2),
        },  # Label
        (audio1[0], np.flipud(audio1[1]))
        if audio1 is not None
        else "files/cantina.wav",  # Audio
        np.flipud(im1) if im1 is not None else "files/cheetah1.jpg",  # Image
        video if video is not None else "files/world.mp4",  # Video
        [
            ("The", "art"),
            ("quick brown", "adj"),
            ("fox", "nn"),
            ("jumped", "vrb"),
            ("testing testing testing", None),
            ("over", "prp"),
            ("the", "art"),
            ("testing", None),
            ("lazy", "adj"),
            ("dogs", "nn"),
            (".", "punc"),
        ]
        + [(f"test {x}", f"test {x}") for x in range(10)],  # HighlightedText
        # [("The testing testing testing", None), ("quick brown", 0.2), ("fox", 1), ("jumped", -1), ("testing testing testing", 0), ("over", 0), ("the", 0), ("testing", 0), ("lazy", 1), ("dogs", 0), (".", 1)] + [(f"test {x}",  x/10) for x in range(-10, 10)],  # HighlightedText
        [
            ("The testing testing testing", None),
            ("over", 0.6),
            ("the", 0.2),
            ("testing", None),
            ("lazy", -0.1),
            ("dogs", 0.4),
            (".", 0),
        ]
        + [(f"test", x / 10) for x in range(-10, 10)],  # HighlightedText
        json.loads(JSONOBJ),  # JSON
        "<button style='background-color: red'>Click Me: "
        + radio
        + "</button>",  # HTML
        "files/titanic.csv",
        df1,  # Dataframe
        np.random.randint(0, 10, (4, 4)),  # Dataframe
        [
            im for im in [im1, im2, im3, im4, "files/cheetah1.jpg"] if im is not None
        ],  # Carousel
        df2,  # Timeseries
    )


iface = gr.Interface(
    fn,
    inputs=[
        gr.inputs.Textbox(default_value="Lorem ipsum", label="Textbox"),
        gr.inputs.Textbox(lines=3, placeholder="Type here..", label="Textbox 2"),
        gr.inputs.Number(label="Number", default_value=42),
        gr.inputs.Slider(default_value=15, minimum=10, maximum=20, label="Slider: 10 - 20"),
        gr.inputs.Slider(maximum=20, step=0.04, label="Slider: step @ 0.04"),
        gr.inputs.Checkbox(label="Checkbox"),
        gr.inputs.CheckboxGroup(default_value=CHOICES[0:2], choices=CHOICES, label="CheckboxGroup"),
        gr.inputs.Radio(label="Radio", choices=CHOICES, default_value=CHOICES[2]),
        gr.inputs.Dropdown(label="Dropdown", choices=CHOICES),
        gr.inputs.Image(label="Image", optional=True),
        gr.inputs.Image(tool="select", label="Image w/ Cropper", optional=True),
        gr.inputs.Image(source="canvas", label="Sketchpad", optional=True),
        gr.inputs.Image(source="webcam", label="Webcam", optional=True),
        gr.inputs.Video(label="Video", optional=True),
        gr.inputs.Audio(label="Audio", optional=True),
        gr.inputs.Audio(source="microphone", label="Microphone", optional=True),
        gr.inputs.File(label="File", optional=True),
        gr.inputs.Dataframe(headers=["Name", "Age", "Gender"], label="Dataframe"),
        gr.inputs.Timeseries(x="time", y=["price", "value"], optional=True),
    ],
    outputs=[
        gr.outputs.Textbox(label="Textbox"),
        gr.outputs.Label(label="Label"),
        gr.outputs.Audio(label="Audio"),
        gr.outputs.Image(label="Image"),
        gr.outputs.Video(label="Video"),
        gr.outputs.HighlightedText(color_map={"punc": "pink", "test 0": "blue"}, label="HighlightedText"),
        gr.outputs.HighlightedText(label="HighlightedText", show_legend=True),
        gr.outputs.JSON(label="JSON"),
        gr.outputs.HTML(label="HTML"),
        gr.outputs.File(label="File"),
        gr.outputs.Dataframe(label="Dataframe"),
        gr.outputs.Dataframe(type="numpy", label="Numpy"),
        gr.outputs.Carousel("image", components=, label="Carousel"),
        gr.outputs.Timeseries(x="time", y=["price", "value"], label="Timeseries"),
    ],
    examples=[
        [
            "the quick brown fox",
            "jumps over the lazy dog",
            10,
            12,
            4,
            True,
            ["foo", "baz"],
            "baz",
            "bar",
            "files/cheetah1.jpg",
            "files/cheetah1.jpg",
            "files/cheetah1.jpg",
            "files/cheetah1.jpg",
            "files/world.mp4",
            "files/cantina.wav",
            "files/cantina.wav",
            "files/titanic.csv",
            [[1, 2, 3], [3, 4, 5]],
            "files/time.csv",
        ]
    ]
    * 3,
    theme="default",
    title="Kitchen Sink",
    description="Try out all the components!",
    article="Learn more about [Gradio](http://gradio.app)",
)

if __name__ == "__main__":
    iface.launch()
