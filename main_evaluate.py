import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--obj', default='hazelnut')
# if shot==0 that means all training data is used
parser.add_argument('--shot', default=10, type=int)
args = parser.parse_args()


def do_evaluate_encoder_multiK(obj):
    from codes.inspection import eval_encoder_NN_multiK
    from codes.networks import EncoderHier

    K_shot = args.shot
    
    enc = EncoderHier(K=64, D=64).cuda()
    enc.load(obj, K_shot)
    enc.eval()

    results = eval_encoder_NN_multiK(enc, obj, K_shot)

    det_64 = results['det_64']
    seg_64 = results['seg_64']

    det_32 = results['det_32']
    seg_32 = results['seg_32']

    det_sum = results['det_sum']
    seg_sum = results['seg_sum']

    det_mult = results['det_mult']
    seg_mult = results['seg_mult']

    print(
        f'| K64 | Det: {det_64:.3f} Seg:{seg_64:.3f} | K32 | Det: {det_32:.3f} Seg: {seg_32:.3f} | sum | Det: {det_sum:.3f} Seg: {seg_sum:.3f} | mult | Det: {det_mult:.3f} Seg: {seg_mult:.3f} ({obj})')

    return results

#########################


def main():
    do_evaluate_encoder_multiK(args.obj)


if __name__ == '__main__':
    main()
