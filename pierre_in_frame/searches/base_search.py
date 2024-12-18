from pprint import pprint

from datasets.registred_datasets import RegisteredDataset
from settings.save_and_load import SaveAndLoad

from settings.labels import Label


class BaseSearch:
    """
    Base class for all search algorithms.
    """

    def __init__(
            self,
            algorithm: str,
            dataset_name: str, trial: int = 1, fold: int = 3,
            n_jobs: int = 1, list_size: int = 10, n_inter: int = 50,
            based_on: str = "RANDOM"
    ):
        """
        Parameters
        """
        self.based_on = based_on
        self.dataset = RegisteredDataset.load_dataset(dataset_name)
        self.algorithm = algorithm
        self.trial = trial
        self.fold = fold
        self.n_inter = n_inter
        self.n_jobs = n_jobs
        self.list_size = list_size
        self.train_list = []
        self.valid_list = []
        self.output = None

    def preparing_data(self):
        """
        Prepares the dataset for pierre search.
        """
        for t in range(1, self.trial + 1):
            for f in range(1, self.fold + 1):
                self.train_list.append(self.dataset.get_train_transactions(
                    fold=f, trial=t
                ))
                if self.based_on in Label.BASED_ON_VALIDATION:
                    self.valid_list.append(self.dataset.get_validation_transactions(
                        fold=f, trial=t
                    ))
                else:
                    self.valid_list.append(self.dataset.get_test_transactions(
                        fold=f, trial=t
                    ))

    def defining_metric_and_save(self):
        """
        Saves the pierre grid search algorithm to a file.
        """
        best_params = {
            "map": 0.0
        }
        for item in self.output:
            if float(best_params["map"]) < float(item["map"]):
                best_params = item
        pprint(best_params)
        # Saving
        SaveAndLoad.save_hyperparameters_recommender(
            best_params=best_params, dataset=self.dataset.system_name, algorithm=self.algorithm
        )
        # Saving
        SaveAndLoad.save_hyperparameters_recommender(
            best_params=self.output, dataset=self.dataset.system_name, algorithm=self.algorithm + "_all"
        )

    @staticmethod
    def defining_metric_and_save_during_run(dataset_name, algorithm, params):
        """
        Saves the pierre grid search algorithm to a file.
        """
        # Load the surprise recommender algorithm
        full_params = {
            "map": 0.0
        }
        try:
            # Load the surprise recommender algorithm
            full_params = SaveAndLoad.load_hyperparameters_recommender(
                dataset=dataset_name, algorithm=algorithm
            )
        except FileNotFoundError:
            # Saving
            SaveAndLoad.save_hyperparameters_recommender(
                best_params=params, dataset=dataset_name, algorithm=algorithm
            )
        if float(full_params["map"]) < float(params["map"]):
            # Saving
            SaveAndLoad.save_hyperparameters_recommender(
                best_params=params, dataset=dataset_name, algorithm=algorithm
            )

    def preparing_recommenders(self):
        """
        This method is to be overridden by subclasses.
        """
        pass

    def fit(self):
        """
        This method fits the random search algorithm to a dataset.
        """
        print("*" * 100)
        print("Algorithm: ", self.algorithm)
        print("Dataset: ", self.dataset.system_name)
        print("Fold: ", self.fold)
        print("Trial: ", self.trial)
        print("*" * 100)

        self.preparing_data()

        self.preparing_recommenders()

        self.defining_metric_and_save()
