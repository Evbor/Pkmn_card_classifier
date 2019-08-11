import luigi
import data

#### global constants
processed_csv_path= 'data\\processed.csv' # name of csv storing filenames and labels of already processed data
raw_csv_path = 'data\\raw.csv' # name of csv storing filenames and labels of unprocessed data
unlabeled_csv_path = 'data\\unlabeled.csv' # name of csv storing filenames of unprocessed unlabeled data
images_path = 'data\\images' # path to file storing images

class GlobalParams(luigi.Config):
	pass

class StartPipeline(luigi.WrapperTask):
	testing_pipeline = luigi.BoolParameter()
	processed_csv = luigi.Parameter(default=processed_csv_path)
	raw_csv = luigi.Parameter(default=raw_csv_path)
	unlabeled_csv = luigi.Parameter(default=unlabeled_csv_path)
	images = luigi.Parameter(default=images_path)
	def run(self):
		raw_data = pd.read_csv(raw_csv)
		processed_data = pd.read_csv(processed_csv)
		unlabeled_data = pd.read_csv(unlabeled_csv)
		if (len(raw_data) >= 200) or testing_pipeline:
			yield MLModel()
		elif len(unlabeled_data) >= 10:
			yield Labeldatayoushitheads()
		elif
if __name__ == '__main__':
	luigi.run()
