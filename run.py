from model.train import train
from model.evaluate import generate_all_plots


def main():
    pipeline, metrics = train()

    print('\nGenerating evaluation plots …')
    generate_all_plots()

    print('\n✅  All done!  Check the saved_model/ folder for:')
    print('     • sentiment_model.pkl')
    print('     • metrics.json')
    print('     • confusion_matrix.png')
    print('     • model_comparison.png')
    print('     • metrics_summary.png')


if __name__ == '__main__':
    main()