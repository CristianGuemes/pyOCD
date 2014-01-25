"""
 mbed CMSIS-DAP debugger
 Copyright (c) 2006-2013 ARM Limited

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

from flash import Flash

flash_algo = { 'load_address' : 0x20000000,
               'instructions' : [
    0xE00ABE00, 0x062D780D, 0x24084068, 0xD3000040, 0x1E644058, 0x1C49D1FA, 0x2A001E52, 0x4770D1F2,
    0xb510493a, 0x60084449, 0xf24c4839, 0x81c15120, 0x1128f64d, 0x880181c1, 0x101f021, 0x48368001,
    0x44484934, 0x3200f44f, 0x21006001, 0x1201e9c0, 0x60c202d2, 0x52a0f04f, 0xf44f6142, 0x61826200,
    0x1020f880, 0x62411e49, 0xf93af000, 0xd0002800, 0xbd102001, 0x47702000, 0x4a28b508, 0x9200447a,
    0x2cff3c1, 0x48244601, 0x44482300, 0xf9d3f000, 0xd0002800, 0xbd082001, 0x4920b508, 0x481e4479,
    0x44483920, 0xf8a1f000, 0x481cb970, 0x4b1c4478, 0x447b3830, 0x48189000, 0xf2402204, 0x4448410c,
    0xf96cf000, 0xd0002800, 0xbd082001, 0x4b13b510, 0x4601447b, 0x3b544810, 0x6280f44f, 0xf0004448,
    0x2800f8b8, 0x2001d000, 0xb538bd10, 0x490b460c, 0x39744479, 0x46019100, 0x46134807, 0x44484622,
    0xf94cf000, 0xd0002800, 0xbd382001, 0x4, 0x40052000, 0x40020000, 0x8, 0xa5,
    0x412, 0x4604b570, 0x25006800, 0x61b7803, 0x2370d5fc, 0x20007003, 0x280ce03a, 0xe8dfd236,
    0xa06f000, 0x1a16120e, 0x2a26221e, 0x6826322e, 0x71f37813, 0x6826e02a, 0x71b37853, 0x6826e026,
    0x71737893, 0x6826e022, 0x713378d3, 0x6826e01e, 0x72f37913, 0x6826e01a, 0x72b37953, 0x6826e016,
    0x72737993, 0x6826e012, 0x723379d3, 0x6826e00e, 0x73f37a13, 0x6826e00a, 0x73b37a53, 0x6826e006,
    0x73737a93, 0x6826e002, 0x73337ad3, 0xb2c01c40, 0xd9c24288, 0x20806821, 0xe0037008, 0x1c416a60,
    0x4780d000, 0x78006820, 0xd5f70600, 0x78006820, 0xd5010681, 0xe0062504, 0xd50106c1, 0xe0022508,
    0xd00007c0, 0x46282510, 0xb508bd70, 0x460b2244, 0x2000f88d, 0x2100466a, 0xbd084798, 0x4614b538,
    0xd002078a, 0x7080f44f, 0x6843bd38, 0xd803428b, 0x441a6882, 0xd80c428a, 0x428b68c3, 0x6902d803,
    0x428a441a, 0x2002d801, 0x1ac9bd38, 0x100f501, 0x1ac9e000, 0xf88d2208, 0xc0a2000, 0x2001f88d,
    0xf88d0a0a, 0xf88d2002, 0x466a1003, 0x47a02103, 0xe92dbd38, 0x460745f8, 0x46164698, 0x2000687b,
    0xf44f198a, 0x428b6580, 0x68bcd803, 0x4294441c, 0x68fbd20d, 0xd803428b, 0x441c693c, 0xd2024294,
    0xe8bd2002, 0x1acc85f8, 0x400f504, 0x1acce000, 0xf1f5fbb4, 0x4111fb05, 0xf44fb111, 0xe7f07080,
    0xf1f5fbb6, 0x6111fb05, 0x2001b1a9, 0xf88de7e9, 0xc20a000, 0x1f88d, 0xf88d0a20, 0xf88d0002,
    0x466a4003, 0x46382103, 0x47984643, 0xd1d82800, 0x442c1b76, 0xf04fe001, 0x2e000a09, 0xe7d0d1e7,
    0x6801b5f0, 0x780a2400, 0xd5fc0612, 0x700a2270, 0x21036802, 0x680171d1, 0x718d2580, 0x21006802,
    0x68037151, 0x711a22fc, 0x73d16802, 0x70156802, 0x78136802, 0xd5fc061b, 0x7a127a56, 0xc0ff002,
    0x4200f44f, 0xf1bc1057, 0xd2110f10, 0xf00ce8df, 0xf0d0a08, 0x8080808, 0x80d1e0f, 0x8080808,
    0xe0056102, 0x42c0f44f, 0x6107e7fa, 0x6101e000, 0x20ff006, 0xd21b2a10, 0xf002e8df, 0xd0b0b0b,
    0x19161310, 0xb0b1e1c, 0xb0b0b0b, 0x5200f44f, 0x61c1e7e6, 0xf44fe00c, 0xe7fa6100, 0x6180f44f,
    0xf44fe7f7, 0xe7f47100, 0x7180f44f, 0x61c5e7f1, 0xbdf04620, 0xe7ec2140, 0xe7ea2120, 0x47fce92d,
    0x46074616, 0x2000461d, 0xf8dd198a, 0x78b8028, 0xf44fd003, 0xe8bd7080, 0x7b387fc, 0x2001d001,
    0x687be7f9, 0xd803428b, 0x441c68bc, 0xd20c4294, 0x428b68fb, 0x693cd803, 0x4294441c, 0x2002d201,
    0x1acce7e9, 0x400f504, 0x1acce000, 0xa06f04f, 0xd0e02e00, 0xa000f88d, 0xf88d0c20, 0xa200001,
    0x2f88d, 0x4003f88d, 0xf88d78e8, 0x78a80004, 0x5f88d, 0xf88d7868, 0x78280006, 0x7f88d,
    0x2107466a, 0x46434638, 0x28004798, 0x1d24d1c3, 0x1d2d1f36, 0xe92de7dc, 0x684641fc, 0xeb019d08,
    0x428e0482, 0x6887d803, 0x428f4437, 0x68c7d80a, 0xd804428f, 0xc010f8d0, 0x428f4467, 0x2002d802,
    0x81fce8bd, 0xd80542a6, 0x44376887, 0xd30142a7, 0xe0091b89, 0x42a668c6, 0x6907d903, 0x42a74437,
    0x1b89d3ed, 0x100f501, 0xfbb12404, 0xfb04f6f4, 0xb1141416, 0x7080f44f, 0x2401e7e2, 0x4000f88d,
    0xf88d0c0c, 0xa0c4001, 0x4002f88d, 0x1003f88d, 0xf88d0a11, 0xf88d1004, 0xf88d2005, 0x466a3006,
    0x47a82106, 0xe7cc, 0xfffffffe, 0x0, 0xffffffff, 0xfffffffe, 0x0, 0x0
                                ],
               'pc_init' : 0x20000020,
               'pc_eraseAll' : 0x20000098,
               'pc_erase_sector' : 0x200000cc,
               'pc_program_page' : 0x200000ea,
               'begin_stack' : 0x20000c00,
               'begin_data' : 0x20001c00,
               'static_base' : 0x200004e0,
               'page_size' : 1024
              };

memoryMapXML =  "<?xml version=\"1.0\"?>" \
                "<!DOCTYPE memory-map PUBLIC \"+//IDN gnu.org//DTD GDB Memory Map V1.0//EN\" \"http://sourceware.org/gdb/gdb-memory-map.dtd\">" \
                "<memory-map>" \
                    "<memory type=\"flash\" start=\"0x0\" length=\"0x20000\"> <property name=\"blocksize\">0x400</property></memory>" \
                    "<memory type=\"ram\" start=\"0x20000000\" length=\"0x4000\"> </memory>" \
                "</memory-map>"


class Flash_k20d50m(Flash):
    
    def __init__(self, target):
        Flash.__init__(self, target, flash_algo, memoryMapXML)
    
