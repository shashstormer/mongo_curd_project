from dataclasses import dataclass
from fastapi.params import Query
from pydantic import BaseModel, Field, field_validator, ValidationError
from typing import Any, Literal


@dataclass
class Validatiors:
    class search(BaseModel):
        field_name: str = Field(Query(...), title="Field Name",
                                description="Vame of field using which field is identified")
        field_value: Any = Field(Query(...), title="Field Value",
                                 description="Value of field using which field is identified")

    # NOTE: this section has been comented to allow none so that we can fetch all records
    # @field_validator('field_value' , mode="before")
    # def notNone(self, value):
    #     if value is None:
    #         raise ValidationError('The Field Value Cannot Be None')
    #     return value

    class delete(BaseModel):
        field_name: str = Field(..., title="Field Name", description="Name of field using which field is identified")
        field_value: Any = Field(..., title="Field Value", description="Value of field using which field is identified")

        @staticmethod
        @field_validator('field_value', mode="before")
        def notNone(value):
            if value is None:
                raise ValidationError('The Field Value Cannot Be None')
            return value

    class update(BaseModel):
        field_name: str = Field(..., title="Field Name", description="Name of field using which field is identified")
        field_value: Any = Field(..., title="Field Value", description="Value of field using which field is identified")
        data: dict = Field(..., title="Data", description="Data to be updated")

        @staticmethod
        @field_validator('field_value', mode="before")
        def notNone(value):
            if value is None:
                raise ValidationError('The Field Value Cannot Be None')
            return value

    class by_id(BaseModel):
        id_: Any = Field(...)

        @staticmethod
        @field_validator('id_', mode="before")
        def notNone(value):
            if value is None:
                raise ValidationError('No Data to ADD')
            return value

    class create(BaseModel):
        data: Any = Field(...)

        @staticmethod
        @field_validator('data', mode="before")
        def notNone(value):
            if value is None:
                raise ValidationError('No Data to ADD')
            return value
