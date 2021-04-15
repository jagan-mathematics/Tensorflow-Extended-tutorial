import pandas as pd
from tfx.types import artifact_utils
from tfx.types import standard_artifacts
from tfx.types import channel_utils
from collections import defaultdict
from ml_metadata.proto import metadata_store_pb2

def display_properties(input):
    data = defaultdict(list)
    for artifact in input:
        properties = artifact.properties
        custom_properties = artifact.custom_properties
        for key, value in properties.items():
            data['artifact id'].append(artifact.id)
            data['type_id'].append(artifact.type_id)
            data['name'].append(key)
            data['is_customproperty'].append(0)
            data['value'].append(value.string_value)

            
        for key, value in custom_properties.items():
            data['artifact id'].append(artifact.id)
            data['type_id'].append(artifact.type_id)
            data['name'].append(key)
            data['is_customproperty'].append(1)
            data['value'].append(value.string_value)
    return pd.DataFrame(data)


def display_types(types):
    table = {'id': [], 'name': []}
    for a_type in types:
        table['id'].append(a_type.id)
        table['name'].append(a_type.name.split('.')[-1])
    return pd.DataFrame(data=table)

def display_artifacts(store, artifacts):
    table = defaultdict(list)
    for a in artifacts:
        table['artifact id'].append(a.id)
        artifact_type = store.get_artifact_types_by_id([a.type_id])[0]
        table['type'].append(artifact_type.name)
        table['uri'].append(a.uri)
        table['create_time_since_epoch'].append(a.create_time_since_epoch)
        table['last_update_time_since_epoch'].append(a.last_update_time_since_epoch)
    return pd.DataFrame(data=table)
    
def display_context(store, artifacts):
    table = defaultdict(list)
    for a in artifacts:
        table['artifact id'].append(a.id)
        artifact_type = store.get_context_types_by_id([a.type_id])[0]
        table['type'].append(artifact_type.name)
        table['name'].append(a.name)
        table['create_time_since_epoch'].append(a.create_time_since_epoch)
        table['last_update_time_since_epoch'].append(a.last_update_time_since_epoch)
    return pd.DataFrame(data=table)

def display_executions(store, artifacts):
    table = defaultdict(list)
    for a in artifacts:
        table['artifact id'].append(a.id)
        artifact_type = store.get_execution_types_by_id([a.type_id])[0]
        table['type'].append(artifact_type.name.split('.')[-1])
        e_state = a.last_known_state
        if e_state == 2:
            table['last_known_state'].append('Running')
        elif e_state == 3:
            table['last_known_state'].append('Success')
        else:
            table['last_known_state'].append(e_state)
        table['create_time_since_epoch'].append(a.create_time_since_epoch)
 
 
def get_latest_executions(store, pipeline_name, component_id = None):
    if component_id is None:
        run_contexts = [
            c for c in store.get_contexts_by_type('run')
            if c.properties['pipeline_name'].string_value == pipeline_name
        ]
    elif isinstance(component_id, list):
        run_contexts = [
            c for c in store.get_contexts_by_type('component_run')
            if c.properties['pipeline_name'].string_value == pipeline_name and
               c.properties['component_id'].string_value in component_id
        ]
    else:  # Find specific component runs.
        run_contexts = [
            c for c in store.get_contexts_by_type('component_run')
            if c.properties['pipeline_name'].string_value == pipeline_name and
               c.properties['component_id'].string_value == component_id
        ]
    if not run_contexts:
        return []
    # Pick the latest run context.
    latest_context = max(run_contexts,
                       key=lambda c: c.last_update_time_since_epoch)
    return store.get_executions_by_context(latest_context.id)

def get_latest_artifacts(store, pipeline_name, component_id = None):
    executions = get_latest_executions(store, pipeline_name, component_id)

    # Fetch all artifacts produced from the given executions.
    execution_ids = [e.id for e in executions]
    events = store.get_events_by_execution_ids(execution_ids)
    artifact_ids = [
      event.artifact_id for event in events
      if event.type == metadata_store_pb2.Event.OUTPUT
    ]
    return store.get_artifacts_by_id(artifact_ids)


def find_latest_artifacts_by_type(store, artifacts, artifact_type):
    try:
        artifact_type = store.get_artifact_type(artifact_type)
    except errors.NotFoundError:
        return []
    filtered_artifacts = [aritfact for aritfact in artifacts
                        if aritfact.type_id == artifact_type.id]
    return [artifact_utils.deserialize_artifact(artifact_type, artifact)
      for artifact in filtered_artifacts]

def visualize_artifacts(artifacts):
    for artifact in artifacts:
        visualization = visualizations.get_registry().get_visualization(
            artifact.type_name)
    if visualization:
        visualization.display(artifact)
        table['last_update_time_since_epoch'].append(a.last_update_time_since_epoch)
    return pd.DataFrame(data=table)

