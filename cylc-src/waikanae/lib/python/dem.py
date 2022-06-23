# -*- coding: utf-8 -*-
"""
Run the geofabrics.processor.HydrologicDemGenerator pipeline
"""

import json
import pathlib
import dotenv
import os
#import geofabrics.processor

def main():
    """ The dem.main function updates sets the LINZ API keys, reads the
    instruction file in, and runs the geofabrics dem processing pipeline.
    This pipeline combines different source information into a
    hydrologically conditioned DEM.
    """

    print('Run the dem task!')

    # Setup the paths
    base_path = pathlib.Path().cwd().parent.parent.parent

    # Setup the LINZ API keys
    dotenv.load_dotenv(base_path / ".env")
    linz_key = os.environ.get("LINZ_API", None)

    # Read in the instruction file
    with open(base_path / "instruction.json", "r") as file_pointer:
        instructions = json.load(file_pointer)

    # Launch the geofabrics processing routine
    '''runner = geofabrics.processor.HydrologicDemGenerator(
        cls.instructions["dem"], debug=False
    )'''


if __name__ == "__main__":
    main()