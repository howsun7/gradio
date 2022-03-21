import numpy as np

import gradio as gr


def transpose(matrix):
    return matrix.T


iface = gr.Interface(
    transpose,
    gr.inputs.Dataframe(row_count=5, col_count=3, datatype="number", type="numpy"),
    "numpy",
    examples=[
        [np.zeros((3, 3)).tolist()],
        [np.ones((2, 2)).tolist()],
        [np.random.randint(0, 10, (3, 10)).tolist()],
        [np.random.randint(0, 10, (10, 3)).tolist()],
        [np.random.randint(0, 10, (10, 10)).tolist()],
    ],
)

iface.test_launch()

if __name__ == "__main__":
    iface.launch()
