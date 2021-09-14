params = {
    'domain': 'Machinemonitoring',
    'buildingBlock': 'MachineTelemetry',
    'aggregate': 'MachineTelemetry',
    'mode': 'write',
    'env': 'dev',
    'layer': {
        'bronzeEventLayer': {
            'inputSchemaFilePath': '../schemas/telemetrySchemaBronze_v1.json',
            'inputSchema': '',
            'storage': {
                'azure': {
                    'blob': {
                        'conString': 'DefaultEndpointsProtocol=https;AccountName=rsrgstefanposs;AccountKey=OVOnLfU8zPzENLCZbKR6LJp/56p456nTmmIuLT8m6v5+0ud8FpuCD6wPmQp9ks0I9emAVDZXiXn+q5ZNik8Z8Q==;EndpointSuffix=core.windows.net'
                    }
                }
            }
        },
        'silverEventLayer': {
            'inputSchemaFilePath': '',
            'inputSchema': '',
            'storage': {
                'azure': {
                    'blob': {
                        'conString': 'DefaultEndpointsProtocol=https;AccountName=rsrgstefanposs;AccountKey=OVOnLfU8zPzENLCZbKR6LJp/56p456nTmmIuLT8m6v5+0ud8FpuCD6wPmQp9ks0I9emAVDZXiXn+q5ZNik8Z8Q==;EndpointSuffix=core.windows.net'
                    }
                }
            }
        },
        'goldEventLayer': {
            'inputSchemaFilePath': '',
            'inputSchema': '',
            'storage': {
                'azure': {
                    'blob': {
                        'conString': 'DefaultEndpointsProtocol=https;AccountName=rsrgstefanposs;AccountKey=OVOnLfU8zPzENLCZbKR6LJp/56p456nTmmIuLT8m6v5+0ud8FpuCD6wPmQp9ks0I9emAVDZXiXn+q5ZNik8Z8Q==;EndpointSuffix=core.windows.net'
                    }
                }
            }
        }
    }
}