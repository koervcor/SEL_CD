
MSTAR = {
  "epoch": 100,
  "num_classes": 10,
  "train_image_path": "./data/mstar/TRAIN/17_DEG/",
  "valid_image_path": "./data/mstar/VAL/17_DEG/",
  "test_image_path": "./data/mstar/TEST/15_DEG/",
  "predict_image_path": "./data/mstar/TEST/",
  "lr": 0.01,
  "delta": 40,
  "gamma": 0.5,
  "step_lr": [10, 30, 60, 80],
  "image_format": "jpeg",
  "model_output_dir": "./chkpt",
  "chkpt": "MSTAR.pth",
  "predict_model": "./chkpt/MSTAR.pth",
  "mean": [0.37918335],
  "std": [0.20051193]
}

OpenSARShip = {
  "epoch": 150,
  "num_classes": 3,
  "train_image_path": "./data/opensarship_3/train/",
  "valid_image_path": "./data/opensarship_3/test/",
  "test_image_path": "./data/opensarship_3/test/",
  "predict_image_path": "./data/opensarship_3/occ/",
  "lr": 0.1,
  "delta": 50,
  "gamma": 0.5,
  "step_lr": [10, 40, 70, 100, 130, 140],
  "image_format": "tif",
  "model_output_dir": "./chkpt",
  "chkpt": "OpenSARShip.pth",
  "predict_model": "./chkpt/OpenSARShip.pth",
  "mean": [0.031222539],
  "std": [0.05072905]
}