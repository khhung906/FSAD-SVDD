obj=(bottle cable capsule carpet grid hazelnut leather metal_nut pill screw tile toothbrush transistor wood zipper)

for o in ${obj[@]}; do
    echo $o
    python main_evaluate.py --obj=$o
    python main_visualize.py --obj=$o --shot=16
done