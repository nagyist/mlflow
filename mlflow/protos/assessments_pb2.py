
import google.protobuf
from packaging.version import Version
if Version(google.protobuf.__version__).major >= 5:
  # -*- coding: utf-8 -*-
  # Generated by the protocol buffer compiler.  DO NOT EDIT!
  # source: assessments.proto
  # Protobuf Python Version: 5.26.0
  """Generated protocol buffer code."""
  from google.protobuf import descriptor as _descriptor
  from google.protobuf import descriptor_pool as _descriptor_pool
  from google.protobuf import symbol_database as _symbol_database
  from google.protobuf.internal import builder as _builder
  # @@protoc_insertion_point(imports)

  _sym_db = _symbol_database.Default()


  from . import databricks_pb2 as databricks__pb2
  from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
  from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


  DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x61ssessments.proto\x12\x12mlflow.assessments\x1a\x10\x64\x61tabricks.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xc6\x01\n\x10\x41ssessmentSource\x12J\n\x0bsource_type\x18\x01 \x01(\x0e\x32/.mlflow.assessments.AssessmentSource.SourceTypeB\x04\xf8\x86\x19\x01\x12\x17\n\tsource_id\x18\x02 \x01(\tB\x04\xf8\x86\x19\x01\"M\n\nSourceType\x12\x1b\n\x17SOURCE_TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05HUMAN\x10\x01\x12\r\n\tLLM_JUDGE\x10\x02\x12\x08\n\x04\x43ODE\x10\x03\"Q\n\x0f\x41ssessmentError\x12\x12\n\nerror_code\x18\x01 \x01(\t\x12\x15\n\rerror_message\x18\x02 \x01(\t\x12\x13\n\x0bstack_trace\x18\x03 \x01(\t\"\xbf\x01\n\x0b\x45xpectation\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.google.protobuf.Value\x12I\n\x10serialized_value\x18\x03 \x01(\x0b\x32/.mlflow.assessments.Expectation.SerializedValue\x1a>\n\x0fSerializedValue\x12\x1c\n\x14serialization_format\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"e\n\x08\x46\x65\x65\x64\x62\x61\x63k\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.google.protobuf.Value\x12\x32\n\x05\x65rror\x18\x03 \x01(\x0b\x32#.mlflow.assessments.AssessmentError\"\xd9\x04\n\nAssessment\x12\x15\n\rassessment_id\x18\x01 \x01(\t\x12\x1d\n\x0f\x61ssessment_name\x18\x02 \x01(\tB\x04\xf8\x86\x19\x01\x12\x10\n\x08trace_id\x18\x03 \x01(\t\x12\x0f\n\x07span_id\x18\x04 \x01(\t\x12\x34\n\x06source\x18\x05 \x01(\x0b\x32$.mlflow.assessments.AssessmentSource\x12/\n\x0b\x63reate_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x34\n\x10last_update_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x30\n\x08\x66\x65\x65\x64\x62\x61\x63k\x18\t \x01(\x0b\x32\x1c.mlflow.assessments.FeedbackH\x00\x12\x36\n\x0b\x65xpectation\x18\n \x01(\x0b\x32\x1f.mlflow.assessments.ExpectationH\x00\x12\x11\n\trationale\x18\x0b \x01(\t\x12\x36\n\x05\x65rror\x18\x0c \x01(\x0b\x32#.mlflow.assessments.AssessmentErrorB\x02\x18\x01\x12>\n\x08metadata\x18\r \x03(\x0b\x32,.mlflow.assessments.Assessment.MetadataEntry\x12\x11\n\toverrides\x18\x0e \x01(\t\x12\x13\n\x05valid\x18\x0f \x01(\x08:\x04true\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x07\n\x05valueB\x19\n\x14org.mlflow.api.proto\x90\x01\x01')

  _globals = globals()
  _builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
  _builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'assessments_pb2', _globals)
  if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\024org.mlflow.api.proto\220\001\001'
    _globals['_ASSESSMENTSOURCE'].fields_by_name['source_type']._loaded_options = None
    _globals['_ASSESSMENTSOURCE'].fields_by_name['source_type']._serialized_options = b'\370\206\031\001'
    _globals['_ASSESSMENTSOURCE'].fields_by_name['source_id']._loaded_options = None
    _globals['_ASSESSMENTSOURCE'].fields_by_name['source_id']._serialized_options = b'\370\206\031\001'
    _globals['_ASSESSMENT_METADATAENTRY']._loaded_options = None
    _globals['_ASSESSMENT_METADATAENTRY']._serialized_options = b'8\001'
    _globals['_ASSESSMENT'].fields_by_name['assessment_name']._loaded_options = None
    _globals['_ASSESSMENT'].fields_by_name['assessment_name']._serialized_options = b'\370\206\031\001'
    _globals['_ASSESSMENT'].fields_by_name['error']._loaded_options = None
    _globals['_ASSESSMENT'].fields_by_name['error']._serialized_options = b'\030\001'
    _globals['_ASSESSMENTSOURCE']._serialized_start=123
    _globals['_ASSESSMENTSOURCE']._serialized_end=321
    _globals['_ASSESSMENTSOURCE_SOURCETYPE']._serialized_start=244
    _globals['_ASSESSMENTSOURCE_SOURCETYPE']._serialized_end=321
    _globals['_ASSESSMENTERROR']._serialized_start=323
    _globals['_ASSESSMENTERROR']._serialized_end=404
    _globals['_EXPECTATION']._serialized_start=407
    _globals['_EXPECTATION']._serialized_end=598
    _globals['_EXPECTATION_SERIALIZEDVALUE']._serialized_start=536
    _globals['_EXPECTATION_SERIALIZEDVALUE']._serialized_end=598
    _globals['_FEEDBACK']._serialized_start=600
    _globals['_FEEDBACK']._serialized_end=701
    _globals['_ASSESSMENT']._serialized_start=704
    _globals['_ASSESSMENT']._serialized_end=1305
    _globals['_ASSESSMENT_METADATAENTRY']._serialized_start=1249
    _globals['_ASSESSMENT_METADATAENTRY']._serialized_end=1296
  # @@protoc_insertion_point(module_scope)

else:
  # -*- coding: utf-8 -*-
  # Generated by the protocol buffer compiler.  DO NOT EDIT!
  # source: assessments.proto
  """Generated protocol buffer code."""
  from google.protobuf import descriptor as _descriptor
  from google.protobuf import descriptor_pool as _descriptor_pool
  from google.protobuf import message as _message
  from google.protobuf import reflection as _reflection
  from google.protobuf import symbol_database as _symbol_database
  # @@protoc_insertion_point(imports)

  _sym_db = _symbol_database.Default()


  from . import databricks_pb2 as databricks__pb2
  from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
  from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


  DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x61ssessments.proto\x12\x12mlflow.assessments\x1a\x10\x64\x61tabricks.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xc6\x01\n\x10\x41ssessmentSource\x12J\n\x0bsource_type\x18\x01 \x01(\x0e\x32/.mlflow.assessments.AssessmentSource.SourceTypeB\x04\xf8\x86\x19\x01\x12\x17\n\tsource_id\x18\x02 \x01(\tB\x04\xf8\x86\x19\x01\"M\n\nSourceType\x12\x1b\n\x17SOURCE_TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05HUMAN\x10\x01\x12\r\n\tLLM_JUDGE\x10\x02\x12\x08\n\x04\x43ODE\x10\x03\"Q\n\x0f\x41ssessmentError\x12\x12\n\nerror_code\x18\x01 \x01(\t\x12\x15\n\rerror_message\x18\x02 \x01(\t\x12\x13\n\x0bstack_trace\x18\x03 \x01(\t\"\xbf\x01\n\x0b\x45xpectation\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.google.protobuf.Value\x12I\n\x10serialized_value\x18\x03 \x01(\x0b\x32/.mlflow.assessments.Expectation.SerializedValue\x1a>\n\x0fSerializedValue\x12\x1c\n\x14serialization_format\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"e\n\x08\x46\x65\x65\x64\x62\x61\x63k\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.google.protobuf.Value\x12\x32\n\x05\x65rror\x18\x03 \x01(\x0b\x32#.mlflow.assessments.AssessmentError\"\xd9\x04\n\nAssessment\x12\x15\n\rassessment_id\x18\x01 \x01(\t\x12\x1d\n\x0f\x61ssessment_name\x18\x02 \x01(\tB\x04\xf8\x86\x19\x01\x12\x10\n\x08trace_id\x18\x03 \x01(\t\x12\x0f\n\x07span_id\x18\x04 \x01(\t\x12\x34\n\x06source\x18\x05 \x01(\x0b\x32$.mlflow.assessments.AssessmentSource\x12/\n\x0b\x63reate_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x34\n\x10last_update_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x30\n\x08\x66\x65\x65\x64\x62\x61\x63k\x18\t \x01(\x0b\x32\x1c.mlflow.assessments.FeedbackH\x00\x12\x36\n\x0b\x65xpectation\x18\n \x01(\x0b\x32\x1f.mlflow.assessments.ExpectationH\x00\x12\x11\n\trationale\x18\x0b \x01(\t\x12\x36\n\x05\x65rror\x18\x0c \x01(\x0b\x32#.mlflow.assessments.AssessmentErrorB\x02\x18\x01\x12>\n\x08metadata\x18\r \x03(\x0b\x32,.mlflow.assessments.Assessment.MetadataEntry\x12\x11\n\toverrides\x18\x0e \x01(\t\x12\x13\n\x05valid\x18\x0f \x01(\x08:\x04true\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x07\n\x05valueB\x19\n\x14org.mlflow.api.proto\x90\x01\x01')



  _ASSESSMENTSOURCE = DESCRIPTOR.message_types_by_name['AssessmentSource']
  _ASSESSMENTERROR = DESCRIPTOR.message_types_by_name['AssessmentError']
  _EXPECTATION = DESCRIPTOR.message_types_by_name['Expectation']
  _EXPECTATION_SERIALIZEDVALUE = _EXPECTATION.nested_types_by_name['SerializedValue']
  _FEEDBACK = DESCRIPTOR.message_types_by_name['Feedback']
  _ASSESSMENT = DESCRIPTOR.message_types_by_name['Assessment']
  _ASSESSMENT_METADATAENTRY = _ASSESSMENT.nested_types_by_name['MetadataEntry']
  _ASSESSMENTSOURCE_SOURCETYPE = _ASSESSMENTSOURCE.enum_types_by_name['SourceType']
  AssessmentSource = _reflection.GeneratedProtocolMessageType('AssessmentSource', (_message.Message,), {
    'DESCRIPTOR' : _ASSESSMENTSOURCE,
    '__module__' : 'assessments_pb2'
    # @@protoc_insertion_point(class_scope:mlflow.assessments.AssessmentSource)
    })
  _sym_db.RegisterMessage(AssessmentSource)

  AssessmentError = _reflection.GeneratedProtocolMessageType('AssessmentError', (_message.Message,), {
    'DESCRIPTOR' : _ASSESSMENTERROR,
    '__module__' : 'assessments_pb2'
    # @@protoc_insertion_point(class_scope:mlflow.assessments.AssessmentError)
    })
  _sym_db.RegisterMessage(AssessmentError)

  Expectation = _reflection.GeneratedProtocolMessageType('Expectation', (_message.Message,), {

    'SerializedValue' : _reflection.GeneratedProtocolMessageType('SerializedValue', (_message.Message,), {
      'DESCRIPTOR' : _EXPECTATION_SERIALIZEDVALUE,
      '__module__' : 'assessments_pb2'
      # @@protoc_insertion_point(class_scope:mlflow.assessments.Expectation.SerializedValue)
      })
    ,
    'DESCRIPTOR' : _EXPECTATION,
    '__module__' : 'assessments_pb2'
    # @@protoc_insertion_point(class_scope:mlflow.assessments.Expectation)
    })
  _sym_db.RegisterMessage(Expectation)
  _sym_db.RegisterMessage(Expectation.SerializedValue)

  Feedback = _reflection.GeneratedProtocolMessageType('Feedback', (_message.Message,), {
    'DESCRIPTOR' : _FEEDBACK,
    '__module__' : 'assessments_pb2'
    # @@protoc_insertion_point(class_scope:mlflow.assessments.Feedback)
    })
  _sym_db.RegisterMessage(Feedback)

  Assessment = _reflection.GeneratedProtocolMessageType('Assessment', (_message.Message,), {

    'MetadataEntry' : _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), {
      'DESCRIPTOR' : _ASSESSMENT_METADATAENTRY,
      '__module__' : 'assessments_pb2'
      # @@protoc_insertion_point(class_scope:mlflow.assessments.Assessment.MetadataEntry)
      })
    ,
    'DESCRIPTOR' : _ASSESSMENT,
    '__module__' : 'assessments_pb2'
    # @@protoc_insertion_point(class_scope:mlflow.assessments.Assessment)
    })
  _sym_db.RegisterMessage(Assessment)
  _sym_db.RegisterMessage(Assessment.MetadataEntry)

  if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\024org.mlflow.api.proto\220\001\001'
    _ASSESSMENTSOURCE.fields_by_name['source_type']._options = None
    _ASSESSMENTSOURCE.fields_by_name['source_type']._serialized_options = b'\370\206\031\001'
    _ASSESSMENTSOURCE.fields_by_name['source_id']._options = None
    _ASSESSMENTSOURCE.fields_by_name['source_id']._serialized_options = b'\370\206\031\001'
    _ASSESSMENT_METADATAENTRY._options = None
    _ASSESSMENT_METADATAENTRY._serialized_options = b'8\001'
    _ASSESSMENT.fields_by_name['assessment_name']._options = None
    _ASSESSMENT.fields_by_name['assessment_name']._serialized_options = b'\370\206\031\001'
    _ASSESSMENT.fields_by_name['error']._options = None
    _ASSESSMENT.fields_by_name['error']._serialized_options = b'\030\001'
    _ASSESSMENTSOURCE._serialized_start=123
    _ASSESSMENTSOURCE._serialized_end=321
    _ASSESSMENTSOURCE_SOURCETYPE._serialized_start=244
    _ASSESSMENTSOURCE_SOURCETYPE._serialized_end=321
    _ASSESSMENTERROR._serialized_start=323
    _ASSESSMENTERROR._serialized_end=404
    _EXPECTATION._serialized_start=407
    _EXPECTATION._serialized_end=598
    _EXPECTATION_SERIALIZEDVALUE._serialized_start=536
    _EXPECTATION_SERIALIZEDVALUE._serialized_end=598
    _FEEDBACK._serialized_start=600
    _FEEDBACK._serialized_end=701
    _ASSESSMENT._serialized_start=704
    _ASSESSMENT._serialized_end=1305
    _ASSESSMENT_METADATAENTRY._serialized_start=1249
    _ASSESSMENT_METADATAENTRY._serialized_end=1296
  # @@protoc_insertion_point(module_scope)

