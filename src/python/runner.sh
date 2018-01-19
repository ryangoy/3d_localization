python main.py --load_probe_output=False
python compute_bbox_accuracy.py ~/cs/datasets/SSNN/buildings/outputs/bbox_predictions.npy ~/cs/datasets/SSNN/buildings/outputs/bbox_test_labels.npy > logs/default.txt
python main.py --num_dot_layers=8
python compute_bbox_accuracy.py ~/cs/datasets/SSNN/buildings/outputs/bbox_predictions.npy ~/cs/datasets/SSNN/buildings/outputs/bbox_test_labels.npy > logs/8dot.txt
python main.py --num_dot_layers=32
python compute_bbox_accuracy.py ~/cs/datasets/SSNN/buildings/outputs/bbox_predictions.npy ~/cs/datasets/SSNN/buildings/outputs/bbox_test_labels.npy > logs/32dot.txt
python main.py --num_epochs=150
python compute_bbox_accuracy.py ~/cs/datasets/SSNN/buildings/outputs/bbox_predictions.npy ~/cs/datasets/SSNN/buildings/outputs/bbox_test_labels.npy > logs/150epochs.txt

python main.py --loc_loss_lambda=0.1
python compute_bbox_accuracy.py ~/cs/datasets/SSNN/buildings/outputs/bbox_predictions.npy ~/cs/datasets/SSNN/buildings/outputs/bbox_test_labels.npy > logs/lllp1.txt
python main.py --jittered_copies=3
python compute_bbox_accuracy.py ~/cs/datasets/SSNN/buildings/outputs/bbox_predictions.npy ~/cs/datasets/SSNN/buildings/outputs/bbox_test_labels.npy > logs/jittered3.txt
python main.py --ppk32 --load_probe_output=False
python compute_bbox_accuracy.py ~/cs/datasets/SSNN/buildings/outputs/bbox_predictions.npy ~/cs/datasets/SSNN/buildings/outputs/bbox_test_labels.npy > logs/ppk32.txt
python main.py --num_kernels=16 --load_probe_output=False
python compute_bbox_accuracy.py ~/cs/datasets/SSNN/buildings/outputs/bbox_predictions.npy ~/cs/datasets/SSNN/buildings/outputs/bbox_test_labels.npy > logs/nk16.txt


