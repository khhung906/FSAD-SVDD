obj=(bottle cable capsule carpet grid hazelnut leather metal_nut pill screw tile toothbrush transistor wood zipper)

for o in ${obj[@]}; do
    echo $o
    python main_train.py --obj=$o --lr=1e-4 --lambda_value=1e-3 --D=64 --epochs=300 --shot=16
    python main_evaluate.py --obj=$o --shot=16
    python main_visualize.py --obj=$o --shot=16
done