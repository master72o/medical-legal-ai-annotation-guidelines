import json, argparse, sys

def validate_domain_annotation(item):
    errors = []
    if 'prompt_id' not in item:
        errors.append("Missing prompt_id")
    if item.get('domain') not in ['Medical', 'Legal']:
        errors.append("Domain must be Medical or Legal")
    if item.get('chosen_response') not in ['Response A', 'Response B', 'TIE']:
        errors.append("Invalid chosen_response")
    if len(item.get('rationale', '')) < 20:
        errors.append("Rationale must be at least 20 characters")
    score = item.get('clinical_or_statutory_accuracy_score')
    if not isinstance(score, int) or score < 1 or score > 5:
        errors.append("Accuracy score must be integer between 1 and 5")
    return errors

def main():
    parser = argparse.ArgumentParser(description="Validate Domain Annotations")
    parser.add_argument("--dataset", required=True)
    args = parser.parse_args()

    with open(args.dataset) as f:
        data = json.load(f)

    total_errors = 0
    for idx, item in enumerate(data):
        errs = validate_domain_annotation(item)
        if errs:
            print(f"Item {idx} ({item.get('prompt_id')}): INVALID -> {errs}")
            total_errors += len(errs)
        else:
            print(f"Item {idx} ({item.get('prompt_id')}): VALID")

    if total_errors == 0:
        print("\nAll domain annotations passed validation!")
        sys.exit(0)
    else:
        print(f"\nFailed with {total_errors} errors.")
        sys.exit(1)

if __name__ == "__main__":
    main()
