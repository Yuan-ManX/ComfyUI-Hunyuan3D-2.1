from hy3dpaint.textureGenPipeline import Hunyuan3DPaintPipeline
from hy3dpaint.textureGenPipeline import Hunyuan3DPaintPipeline, Hunyuan3DPaintConfig
from hy3dshape.hy3dshape.pipelines import Hunyuan3DDiTFlowMatchingPipeline


class LoadHunyuan3DModel:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "model_path": ("STRING", {"default": "tencent/Hunyuan3D-2.1"}),
                "device": (["cuda", "cpu"], {"default": "cuda"}),
            }
        }

    RETURN_TYPES = ("MODEL",)
    RETURN_NAMES = ("model",)
    FUNCTION = "load_model"
    CATEGORY = "Hunyuan3D-2.1"

    def load_model(self, model_path):
        model = Hunyuan3DDiTFlowMatchingPipeline.from_pretrained('tencent/Hunyuan3D-2.1')
        
        return (model,)


class LoadHunyuan3DImage:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image_path": ("STRING", {"default": "assets/demo.png"}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = "input_image"
    CATEGORY = "Hunyuan3D-2.1"

    def input_image(self, image_path):
        image = image_path
        return (image,)


class Hunyuan3DShapeGeneration:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model": ("MODEL",),
                "image": ("IMAGE",),
            }
        }

    RETURN_TYPES = ("MESH",)
    RETURN_NAMES = ("mesh_untextured",)
    FUNCTION = "generate"
    CATEGORY = "Hunyuan3D-2.1"

    def generate(self, model, image):
        shape_pipeline = model
        mesh_untextured = shape_pipeline(image=image)[0]
        
        return (mesh_untextured,)


class Hunyuan3DTexureSynthsis:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
                "mesh_untextured": ("MESH",),
                "max_num_view": ("INT", {"default": 6}),
                "resolution": ("INT", {"default": 512}),
            }
        }

    RETURN_TYPES = ("TEXURE",)
    RETURN_NAMES = ("mesh_textured",)
    FUNCTION = "generate"
    CATEGORY = "Hunyuan3D-2.1"

    def generate(self, image, mesh_untextured, max_num_view, resolution):
        mesh_path = mesh_untextured
        paint_pipeline = Hunyuan3DPaintPipeline(Hunyuan3DPaintConfig(max_num_view=max_num_view, resolution=resolution))
        mesh_textured = paint_pipeline(mesh_path, image_path=image)
        
        return (mesh_textured,)


