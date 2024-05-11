# pip install flask
# pip install flask_cors
from flask import Flask, Response
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

fake_api_new = [
    [
        {
            'id': 1,
            'Name': 'Видеокарта MSI RTX 4080 Super Gaming X Slim, 16 GB, GeForce RTX 4080 Super',
            'Chipset_Model': 'GeForce RTX 4080 Super',
            'Playback_frequency_in_OC_mode': '2640 MHz',
            'Gaming_Mode_Video_Processor_Frequency': '2610 MHz',
            'Video_memory_frequency_MHz': '23000',
            'Video_Recording_Type': 'GDDR',
            'Video_memory_capacity': '16 GB',
            'Video_memory_bus_bit_rate': '256 bits',
            'Number_of_universal_processors': '10240',
            'Connectors': 'HDMI x2, DisplayPort x 3',
            'Img_url': 'https://c.dns-shop.kz/thumb/st4/fit/500/500/9066f6442ec4cba47b62c2918de98c70/5c164a611c664041b8fb948899651e588766c6569413ee935fa8ec8a479ccbbc.png.webp',
            'Price': 649990
        },
        {
            'id': 2,
            'Name': 'Видеокарта Palit GeForce GTX 1660 SUPER GamingPro [NE6166S018J9-1160A-1]',
            'Chipset_Model': 'Palit GeForce GTX 1660 SUPER GamingPro',
            'Playback_frequency_in_OC_mode': '1785 MHz',
            'Gaming_Mode_Video_Processor_Frequency': '1785 MHz',
            'Video_memory_frequency_MHz': '14000',
            'Video_Recording_Type': 'GDDR6',
            'Video_memory_capacity': '6 GB',
            'Video_memory_bus_bit_rate': '192 bits',
            'Number_of_universal_processors': '14000',
            'Connectors': 'HDMI x2, DisplayPort x 2',
            'Img_url': 'https://c.dns-shop.kz/thumb/st1/fit/500/500/9943d1de8e70cc7955eba64373c29b48/927b7196d085e0d62c46e2ff5f8fe3006f23f1de4de6065670f0206438ae0aac.jpg.webp',
            'Price': 120000
        },
        {
            'id': 3,
            'Name': 'Видеокарта ZOTAC GeForce RTX 3060 GAMING Twin Edge [ZT-A30600E-10M]',
            'Chipset_Model': 'ZOTAC GeForce RTX 3060 GAMING Twin Edge',
            'Playback_frequency_in_OC_mode': '1777 MHz',
            'Gaming_Mode_Video_Processor_Frequency': '1777  MHz',
            'Video_memory_frequency_MHz': '15000',
            'Video_Recording_Type': 'GDDR6',
            'Video_memory_capacity': '12 GB',
            'Video_memory_bus_bit_rate': '192 bits',
            'Number_of_universal_processors': '15000',
            'Connectors': 'HDMI x2, DisplayPort x 2',
            'Img_url': 'https://c.dns-shop.kz/thumb/st4/fit/500/500/0b37bf7af4755fa7c8f7274cd36ce115/e1f7710933c1366dd8871d1a0db02c1a9dd621a249dae4388637011b8a9c6cea.jpg.webp',
            'Price': 160000
        }
    ],
    [
        {
            'id': 1,
            'Name': 'Процессор Intel Core i5 14400F, LGA1700, OEM',
            'Processor_Type': 'Core i5',
            'Socket': 'LGA 1700',
            'Total_number_of_cores': '10',
            'Number_of_threads': '16',
            'Clock_frequency': '2.5 GHz',
            'Microarchitecture': 'Raptor Lake',
            'L3_cache_size': '20 MB',
            'Integrated_graphics_system': 'Нет',
            'Process_technology': '10 nm',
            'TDP': '65W',
            'Img_url': 'https://c.dns-shop.kz/thumb/st1/fit/500/500/3a2e201504b9b5519c5138024bc6af71/11b77c2d7ded215dcc9aae61c4328753088c368061a1b4524cd5ee6e5da97453.jpg.webp',
            'Price': 111990
        },
        {
            'id': 2,
            'Name': 'Процессор Intel Core i5-12400F OEM',
            'Processor_Type': 'Core i5',
            'Socket': 'LGA 1700',
            'Total_number_of_cores': '12',
            'Number_of_threads': '16',
            'Clock_frequency': '2.4 GHz',
            'Microarchitecture': 'Raptor Lake',
            'L3_cache_size': 'q8 MB',
            'Integrated_graphics_system': '0',
            'Process_technology': '12 nm',
            'TDP': '55W',
            'Img_url': 'https://c.dns-shop.kz/thumb/st4/fit/500/500/41c0678f76a1b36e262b5b016216b186/200e4a08e74afcc3cf1d54d47b758cbbf14c71973a64009553347d2b234b5af4.jpg.webp',
            'Price': 60790
        },
        {
            'id': 3,
            'Name': 'Процессор Intel Core i9-13900K OEM',
            'Processor_Type': 'Core i9',
            'Socket': 'LGA 1700',
            'Total_number_of_cores': '24',
            'Number_of_threads': '26',
            'Clock_frequency': '5.8 GHz',
            'Microarchitecture': 'Raptor Lake',
            'L3_cache_size': 'q8 MB',
            'Integrated_graphics_system': '0',
            'Process_technology': '40 nm',
            'TDP': '108W',
            'Img_url': 'https://c.dns-shop.kz/thumb/st4/fit/500/500/83ea9852bd24fee7147130d4bb1ba0fd/66e4986f12ca85239f674009ee5bacf714e92c3510d948945d966f14dabf1000.jpg.webp',
            'Price': 316000
        },
    ],
    [
        {
            'id': 1,
            'Name': 'Материнская плата MSI MAG Z790 TOMAHAWK WIFI',
            'Socket': 'LGA 1700',
            'Total_number_of_cores': '24',
            'Number_of_threads': '26',
            'Clock_frequency': '5.8 GHz',
            'Microarchitecture': 'Raptor Lake',
            'L3_cache_size': 'q8 MB',
            'Integrated_graphics_system': '0',
            'Process_technology': '40 nm',
            'TDP': '108W',
            'Img_url': 'https://c.dns-shop.kz/thumb/st4/fit/500/500/9da7700354de1053bb245cbf03f6e49d/1236dd874c3c7820f259b00db2ef902196ce348adad5bd8896c8f5f3ba2eabb8.jpg.webp',
            'Price': 148900
        },
        {
            'id': 2,
            'Name': 'Материнская плата MSI X670E GAMING PLUS WIFI',
            'Socket': 'LGA 1700',
            'Total_number_of_cores': '24',
            'Number_of_threads': '26',
            'Clock_frequency': '5.8 GHz',
            'Microarchitecture': 'Raptor Lake',
            'L3_cache_size': 'q8 MB',
            'Integrated_graphics_system': '0',
            'Process_technology': '40 nm',
            'TDP': '108W',
            'Img_url': 'https://c.dns-shop.kz/thumb/st1/fit/500/500/e76a245712b73d6ed988aeba4ee8eab2/dd8819319fb0f858cf4745e9a20eb38e80281ebe9dd378595a4ac7ae61b3d50d.jpg.webp',
            'Price': 155990
        },
        {
            'id': 3,
            'Name': 'Материнская плата ASRock B650M Pro RS',
            'Socket': 'LGA 1700',
            'Total_number_of_cores': '24',
            'Number_of_threads': '26',
            'Clock_frequency': '5.8 GHz',
            'Microarchitecture': 'Raptor Lake',
            'L3_cache_size': 'q8 MB',
            'Integrated_graphics_system': '0',
            'Process_technology': '40 nm',
            'TDP': '108W',
            'Img_url': 'https://c.dns-shop.kz/thumb/st1/fit/500/500/a7471569e967644352ffed3e60f3a87f/2eba027c1975912c0203207c855de7826035443f55146b6308fb84b213fc3f0a.jpg.webp',
            'Price': 65000
        },
    ],
]

@app.route('/', methods=['GET'])
def get_fake_obj():
    fake_api = fake_api_new
    response_data = json.dumps(fake_api, ensure_ascii=False)
    return Response(response=response_data, content_type="application/json; charset=utf-8")


if __name__ == '__main__':
    app.run(debug=True)
