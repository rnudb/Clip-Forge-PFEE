import os
from . import test_post_clip
from .test_post_clip import main

class ClipForge:
    def __init__(self, current_path : str) -> None:
        self.args = ["--checkpoint_dir_base", "\"./exps/models/autoencoder\"", "--checkpoint", "best_iou", "--checkpoint_nf", "best", "--experiment_mode", "save_voxel_on_query", "--checkpoint_dir_prior", "\"./exps/models/prior\"", "--threshold", "\"0.1\"", "--output_dir", "\"./exps/output\""]
        self.query_prefix = "--text_query"
        self.current_path = current_path

        # Check that exps folder exists
        if not os.path.exists("./exps"):
            # Prepare exp data
            os.system("wget https://clip-forge-pretrained.s3.us-west-2.amazonaws.com/exps.zip")
            cmd = "unzip exps.zip -d " + current_path
            os.system(cmd)
            os.system("rm exps.zip")

    def query(self, queries: list = None) -> None:
        if queries is None:
            return

        # Format queries
        for i in range(len(queries)):
            queries[i] = "\"" + queries[i] + "\""

        # Build final args
        args = self.args + [self.query_prefix] + queries
        for arg in args:
            if arg.startswith("\"./\""):
                arg = arg[1:-1] # Remove quotes
                arg = arg[1:] # Remove .
                arg = os.path.join(self.current_path, arg) # Add current path
                arg = "\"" + arg + "\"" # Add quotes
            print(arg, end=" ")

        # Run query
        main(args)

        # Files will be saved in ./voxels_<query>.obj in pickle format
        
