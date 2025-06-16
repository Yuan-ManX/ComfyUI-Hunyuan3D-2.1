from .nodes import LoadHunyuan3DModel, LoadHunyuan3DImage, Hunyuan3DShapeGeneration, Hunyuan3DTexureSynthsis

NODE_CLASS_MAPPINGS = {
    "LoadHunyuan3DModel": LoadHunyuan3DModel,
    "LoadHunyuan3DImage": LoadHunyuan3DImage,
    "Hunyuan3DShapeGeneration": Hunyuan3DShapeGeneration,
    "Hunyuan3DTexureSynthsis": Hunyuan3DTexureSynthsis,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LoadHunyuan3DModel": "Load Hunyuan3D Model",
    "LoadHunyuan3DImage": "Load Hunyuan3D Image",
    "Hunyuan3DShapeGeneration": "Hunyuan3D Shape Generation",
    "Hunyuan3DTexureSynthsis": "Hunyuan3D Texure Synthsis",
} 

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
