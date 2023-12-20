import argparse

from attr_rich import attr_rich
from attr_rich_hm_ds_hgrn import attr_rich_hm_ds_hgrn
from attr_rich_cmn_nbs_hgrn import attr_rich_cmn_nbs_hgrn
from graph_gen import graph_gen
from util import compare_dictionaries


# Define the main function
def main():

    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(
        description="Run the attrRich function with parameters."
    )

    # Define command-line arguments
    parser.add_argument("iteration", type=int, help="number of iterations")
    parser.add_argument("n", type=int, help="number of user nodes")
    parser.add_argument("p", type=float, help="user-user edge generating probability")
    parser.add_argument("su", type=float, help="user-user edge selecting probability")
    parser.add_argument("m", type=int, help="number of attribute nodes")
    parser.add_argument("q", type=float, help="user-attr edge generating probability")
    parser.add_argument("sa", type=float, help="user-attr edge selecting probability")
    # parser.add_argument("x", type=float, help="anchor threshold")
    # parser.add_argument("y", type=float, help="match threshold")

    # Parse the command-line arguments
    args = parser.parse_args()

    overall_true_count = 0
    overall_false_count = 0
    overall_miss_count = 0
    overall_accuracy = 0

    print("In\tn\tp\tsu\tq\tm\tsa\tTrue\tFalse\tMiss\tAccuracy")

    for i in range(args.iteration):
        g1, g2prime, node_mapping, num_users = graph_gen(
            args.n, args.p, args.su, args.m, args.q, args.sa,
        )
        # Call the attrRich function
        # Options:
        # 1. attr_rich(): the original attrRich algorithm proposed in the paper using thresholds
        # 2. attr_rich_hm_ds_hgrn(): Using Hungarian Algorithm with cost matrix being the number of
        # common attributes between each user-user pair
        # 3. attr_rich_cmn_nbs_hgrn().py: Using Hungarian Algorithm with cost matrix being the number of
        # common attributes between each user-user pair
        results = attr_rich_cmn_nbs_hgrn(g1, g2prime, num_users)
        metrics = compare_dictionaries(node_mapping, results)

        overall_true_count += metrics[0]
        overall_false_count += metrics[1]
        overall_miss_count += metrics[2]
        overall_accuracy += metrics[3]

        i += 1

    overall_metrics = [
        overall_true_count / args.iteration,
        overall_false_count / args.iteration,
        overall_miss_count / args.iteration,
        overall_accuracy / args.iteration,
    ]

    # Print the result or perform any further actions
    print(
        f"{args.n * args.p * args.su ** 2 + args.m * args.q * args.sa ** 2}"
        f"\t{args.n}\t{args.p}\t{args.su}\t{args.m}\t{args.q}\t{args.sa}"
        f"\t{overall_metrics[0]}\t{overall_metrics[1]}\t{overall_metrics[2]}\t{overall_metrics[3]}"
    )


if __name__ == "__main__":
    main()
