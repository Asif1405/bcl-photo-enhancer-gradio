import gradio as gr
from run_pe import run_inference


def main():
    demo = gr.Interface(
        run_inference,
        inputs=[
            gr.inputs.Image(label="Input Image"),
            gr.inputs.Checkbox(label="Repair Scratch"),
            gr.inputs.Checkbox(label="Colorize"),
            gr.inputs.Checkbox(label="Denoise"),
            gr.inputs.Checkbox(label="Deblur"),
            gr.inputs.Checkbox(label="Image Upscale"),
            gr.inputs.Slider(label="Scale", default=1.0, minimum=1.0, maximum=10.0, step=1.0),
            gr.inputs.Checkbox(label="Face Restore"),
            gr.inputs.Checkbox(label="AI Enhance"),
            gr.inputs.Checkbox(label="Low Light Enhance"),
            gr.inputs.Checkbox(label="White Balance"),
            gr.inputs.Checkbox(label="Color Balance"),
            gr.inputs.Checkbox(label="Remove Artifacts"),
            gr.inputs.Checkbox(label="Derain"),
        ],
        outputs=[
            gr.outputs.File(label="Output Zip"),
            gr.outputs.Image(label="Output Image 1", type="pil"),
            gr.outputs.Image(label="Output Image 2", type="pil"),
            gr.outputs.Image(label="Output Image 3", type="pil"),
            gr.outputs.Image(label="Output Image 4", type="pil"),
        ],
    )
    demo.launch(
        server_name="0.0.0.0",
        server_port=3000
    )


if __name__ == "__main__":
    main()
