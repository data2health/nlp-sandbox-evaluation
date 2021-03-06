# Remove datanode database first
docker volume rm data-node_database-data
# Start data node

cd examples
python push_dataset.py

# Get annotation store
nlp-cli datanode get-annotation-store --dataset_id test-dataset --annotation_store_id goldstandard --data_node_host http://localhost:8080/api/v1

# List annotations
nlp-cli datanode list-annotations --dataset_id test-dataset --annotation_store_id goldstandard --data_node_host http://localhost:8080/api/v1

# list notes
nlp-cli datanode list-notes --dataset_id test-dataset \
                             --fhir_store_id evaluation \
                             --data_node_host http://localhost:8080/api/v1

nlp-cli datanode list-notes --dataset_id test-dataset --fhir_store_id evaluation --data_node_host http://localhost:8080/api/v1 --output example_note.json

# get annotation
nlp-cli datanode get-annotation --annotation_id 110-01 \
                                 --dataset_id test-dataset \
                                 --annotation_store_id goldstandard \
                                 --data_node_host http://localhost:8080/api/v1 

# Get json
nlp-cli datanode get-annotation --annotation_id 110-01 \
                                 --dataset_id test-dataset \
                                 --annotation_store_id goldstandard \
                                 --data_node_host http://localhost:8080/api/v1 \
                                 --output test.json


# Store annotations
nlp-cli datanode store-annotations --dataset_id test-dataset \
                                    --annotation_store_id testing-more \
                                    --annotation_json test_store_annotations.json \
                                    --data_node_host http://localhost:8080/api/v1

nlp-cli datanode get-annotation --annotation_id name \
                                 --dataset_id test-dataset \
                                 --annotation_store_id testing-more \
                                 --data_node_host http://localhost:8080/api/v1

# Start date-annotator-example
nlp-cli evaluate get-tool --annotator_host http://localhost:80/api/v1

nlp-cli evaluate check-url --url http://localhost:80/api/v1/ui

nlp-cli evaluate annotate-note --annotator_host http://localhost:80/api/v1 \
                               --note_json example_note.json \
                               --annotator_type date

nlp-cli evaluate prediction --pred_filepath test/data/new_prediction.json \
                            --gold_filepath test/data/new_goldstandard.json \
                            --eval_type person