import os
from . import test_post_clip
from .test_post_clip import main

class ClipForge:
    def __init__(self, exps_path : str = None) -> None:
        self.args = ["--checkpoint_dir_base", "\"./exps/models/autoencoder\"", "--checkpoint", "best_iou", "--checkpoint_nf", "best", "--experiment_mode", "save_voxel_on_query", "--checkpoint_dir_prior", "\"./exps/models/prior\"", "--threshold", "\"0.1\"", "--output_dir", "\"./exps/output\""]
        self.query_prefix = "--text_query"

        # Check that exps folder exists
        if not os.path.exists("./exps"):
            # Prepare exp data
            os.system("wget https://clip-forge-pretrained.s3.us-west-2.amazonaws.com/exps.zip")
            cmd = "unzip exps.zip"
            if exps_path is not None:
                cmd += " -d "
                cmd += exps_path

            os.system(cmd)

    def query(self, queries: list = None) -> None:
        if queries is None:
            return

        # Format queries
        for i in range(len(queries)):
            queries[i] = "\"" + queries[i] + "\""

        # Run query
        main(self.args + [self.query_prefix] + queries)

        # Files will be saved in ./voxels_<query>.obj in pickle format
        
