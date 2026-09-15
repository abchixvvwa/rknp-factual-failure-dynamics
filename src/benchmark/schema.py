import json
from datetime import date
from typing import Literal

from pydantic import BaseModel, ConfigDict, HttpUrl, field_validator, model_validator

CATEGORIES = ("history", "geography", "science", "culture", "kazakhstan", "adversarial_false_premise")


class Fact(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)
    fact_id: str
    category: Literal["history", "geography", "science", "culture", "kazakhstan", "adversarial_false_premise"]
    difficulty: str
    question_type: Literal["entity", "numeric", "date", "direct_fact", "false_premise"]
    question_en: str
    question_ru: str
    question_kk: str
    canonical_answer: str
    acceptable_aliases_json: str
    false_premise: bool
    source_url: HttpUrl
    source_title: str
    source_publisher: str
    source_accessed_date: date
    notes: str = ""
    verified_by_human: bool

    @field_validator("fact_id", "difficulty", "question_en", "question_ru", "question_kk",
                     "canonical_answer", "source_title", "source_publisher")
    @classmethod
    def not_empty(cls, value):
        if not value:
            raise ValueError("Must not be blank")
        return value

    @field_validator("acceptable_aliases_json")
    @classmethod
    def aliases_are_strings(cls, value):
        aliases = json.loads(value)
        if not isinstance(aliases, list) or any(not isinstance(x, str) or not x.strip() for x in aliases):
            raise ValueError("Aliases must be a JSON list of non-empty strings (possibly empty)")
        return value

    @field_validator("source_accessed_date")
    @classmethod
    def not_future(cls, value):
        if value > date.today():
            raise ValueError("Source access date is in the future")
        return value

    @model_validator(mode="after")
    def consistent_premise(self):
        if self.false_premise != (self.question_type == "false_premise"):
            raise ValueError("false_premise and question_type disagree")
        if self.category == "adversarial_false_premise" and not self.false_premise:
            raise ValueError("Adversarial false-premise category requires false_premise=true")
        return self

    def csv_row(self):
        row = self.model_dump(mode="json")
        for key in ("verified_by_human", "false_premise"):
            row[key] = str(row[key]).lower()
        return row
