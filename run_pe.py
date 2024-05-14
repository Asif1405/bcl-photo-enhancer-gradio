from PIL import Image
import json
import zipfile
import sys

def run_inference(
    test_image,
    repair_scratch,
    colorize,
    denoise,
    deblur,
    upscale,
    scale,
    face_restore,
    face_enhance,
    light_balance,
    white_balance,
    color_balance,
    remove_artifacts,
    derain,
):
    from PE_4_3_24.PhotoEnhance.PhotoEnhancer import PhotoEnhancer
    photo_enhancer = PhotoEnhancer()
    image = Image.fromarray(test_image)
    print(repair_scratch)
    # Read the contents of the temp file
    # print(test_obj)
    # config_info = [

    # ]
    # print(config_info)
    # with open(config_info, 'r') as f:
    #     test_json_obj = json.load(f)
    # print(test_json_obj)
    # print(type(test_json_obj))
    test_images_array = []
    test_images_array = [image]
    # for item in test_json_obj:
    #     print(item)
    #     if 'scale' in item:
    #         item['scale'] = float(item['scale'])
    # with StdoutCapture() as captured_output:
    test_json_obj = []
    if repair_scratch:
        test_json_obj.append(
            {
                "name": "repair_scratch"
            })
    if colorize:
        test_json_obj.append(
            {
                "name": "colorize"
            })
    if denoise:
        test_json_obj.append(
            {
                "name": "denoise"
            })
    if deblur:
        test_json_obj.append(
            {
                "name": "deblur"
            })
    if upscale:
        test_json_obj.append(
            {
                "name": "upscale",
                "scale": scale
            })
    if face_restore:
        test_json_obj.append(
            {
                "name": "face_restore"
            })
    if face_enhance:
        test_json_obj.append(
            {
                "name": "face_enhance"
            })
    if light_balance:
        test_json_obj.append(
            {
                "name": "light_balance"
            })
    if white_balance:
        test_json_obj.append(
            {
                "name": "white_balance"
            })
    if color_balance:
        test_json_obj.append(
            {
                "name": "color_balance"
            })
    if remove_artifacts:
        test_json_obj.append(
            {
                "name": "remove_artifacts"
            })
    if derain:
        test_json_obj.append(
            {
                "name": "derain"
            })
        
    out_images_array = photo_enhancer.enhance(images=test_images_array, config_json=test_json_obj)
        # console_output = captured_output.getvalue()
    # zip the images and return
    with zipfile.ZipFile('output.zip', 'w') as out_zip:
        for i, img in enumerate(out_images_array):
            img.save(f'test_out_{i}.png')
            out_zip.write(f'test_out_{i}.png')
    # print(console_output)
    # return 'output.zip', console_output
    return 'output.zip', out_images_array[0], out_images_array[1] if len(out_images_array) > 1 else None, out_images_array[2] if len(out_images_array) > 2 else None, out_images_array[3] if len(out_images_array) > 3 else None
