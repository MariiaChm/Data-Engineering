# coding=utf-8

from __init__ import *


@app.route('/', methods=['POST'])
def handle_post_request() -> str:
    # get data from post request
    data: dict = request.json

    raw_dir: str = data.get('raw_dir')
    if not raw_dir:
        abort(400, 'raw_dir is not set')
    stg_dir: str = data.get('stg_dir')
    if not stg_dir:
        abort(400, 'stg_dir is not set')

    create_or_clear_directory(stg_dir)

    # get files to be converted
    for file_name in os.listdir(raw_dir):
        target_file_name: str = file_name[:-4] + 'avro'

        print(f"got {file_name} to convert")

        with open(os.path.join(raw_dir, file_name), 'r') as f:
            json_records: list[str] = f.readlines()

            records: list[dict] = [json.loads(record) for record in json_records]

        with open(os.path.join(stg_dir, target_file_name), 'wb') as result_file:
            fastavro.writer(result_file, schemas.sales_schema, records)

    return 'data converted to avro'


if __name__ == '__main__':
    app.run(port=8082)
