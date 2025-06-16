# ComfyUI-Hunyuan3D-2.1

ComfyUI-Hunyuan3D-2.1 is now available in ComfyUI, [Hunyuan3D-2.1](https://github.com/Tencent-Hunyuan/Hunyuan3D-2.1) is a scalable 3D asset creation system that advances state-of-the-art 3D generation through two pivotal innovations: Fully Open-Source Framework and Physically-Based Rendering (PBR) Texture Synthesis.



## Installation

1. Make sure you have ComfyUI installed

2. Clone this repository into your ComfyUI's custom_nodes directory:
```
cd ComfyUI/custom_nodes
git clone https://github.com/Yuan-ManX/ComfyUI-Hunyuan3D-2.1.git
```

3. Install dependencies:
```
cd ComfyUI-Hunyuan3D-2.1

pip install torch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1 --index-url https://download.pytorch.org/whl/cu124
pip install -r requirements.txt

cd hy3dpaint/custom_rasterizer
pip install -e .
cd ../..
cd hy3dpaint/DifferentiableRenderer
bash compile_mesh_painter.sh
cd ../..
```


## Model


### Download Pretrained Models


It takes 10 GB VRAM for shape generation, 21GB for texture generation and 29GB for shape and texture generation in total.


| Model                      | Description                 | Date       | Size | Huggingface                                                                               |
|----------------------------|-----------------------------|------------|------|-------------------------------------------------------------------------------------------| 
| Hunyuan3D-Shape-v2-1         | Image to Shape Model        | 2025-01-21 | 3.3B | [Download](https://huggingface.co/tencent/Hunyuan3D-2.1/tree/main/hunyuan3d-dit-v2-1)         |
| Hunyuan3D-Paint-v2-1       | Texture Generation Model    | 2025-01-21 | 2B | [Download](https://huggingface.co/tencent/Hunyuan3D-2.1/tree/main/hunyuan3d-paint-v2-1)       |

