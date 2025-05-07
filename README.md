# Stable Diffusion Workflow for Consistent Characters

This project explores the best combination (at the time) and sequence of conditioning techniques needed to generate consistent character designs across different generations.

[Thesis](https://github.com/TheAughat/fyp_comics/blob/main/Consistent%20Characters%20SD%20Thesis%20Final.pdf) included within repository.

---

HuggingFace Links:
- Trained checkpoint models: [comicpanel](https://huggingface.co/TheAughat/comicpanel) and [comicpage4](https://huggingface.co/TheAughat/comicpage4)
- Trained character LoRA: [yellowjacketboylei](https://huggingface.co/TheAughat/yellowjacketboylei)

Code references:
- TheLastBen's [fast-stable-diffusion](https://colab.research.google.com/github/TheLastBen/fast-stable-diffusion/blob/main/fast_stable_diffusion_AUTOMATIC1111.ipynb) \(based on the Automatic1111 [WebUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui)\) and [fast-dreambooth](https://colab.research.google.com/github/TheLastBen/fast-stable-diffusion/blob/main/fast-DreamBooth.ipynb)
- Kohya_SS [LoRA trainers](https://github.com/kohya-ss/sd-scripts) and [wrapper notebook](https://colab.research.google.com/github/hollowstrawberry/kohya-colab/blob/main/Lora_Trainer.ipynb) by hollowstrawberry
- Two more DreamBooth trainer notebooks, [the first](https://colab.research.google.com/github/ShivamShrirao/diffusers/blob/main/examples/dreambooth/DreamBooth_Stable_Diffusion.ipynb) by ShivamShrirao and [the second](https://colab.research.google.com/github/JoePenna/Dreambooth-Stable-Diffusion/blob/main/dreambooth_google_colab_joepenna.ipynb) by JoePenna.