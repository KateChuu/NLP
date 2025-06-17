import argparse
import json
from sklearn.metrics import classification_report

def main(args):
    # Load prediction and ground truth files
    try:
        predictions = json.load(open(args.predictions))
    except:
        print("Error loading predictions JSON file:", args.predictions)
        raise SystemExit

    try:
        groundtruth = json.load(open(args.groundtruth))
    except:
        print("Error loading groundtruth JSON file:", args.groundtruth)
        raise SystemExit

    y_true = []
    y_pred = []

    for claim_id, gt in groundtruth.items():
        if claim_id in predictions:
            pred_label = predictions[claim_id].get("claim_label")
            true_label = gt.get("claim_label")

            if pred_label is not None and true_label is not None:
                y_true.append(true_label)
                y_pred.append(pred_label)

    if not y_true or not y_pred:
        print("No valid prediction-label pairs found.")
        return

    # Print classification report
    print("\nClassification Report:")
    print(classification_report(
        y_true,
        y_pred,
        digits=2,
        zero_division=0  # avoid divide-by-zero warnings
    ))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate classification report from claim prediction and ground truth files.")
    parser.add_argument("--predictions", required=True, help="Path to predictions JSON")
    parser.add_argument("--groundtruth", required=True, help="Path to groundtruth JSON")
    args = parser.parse_args()

    main(args)
