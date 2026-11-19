from __future__ import annotations

str_or_none = str | None

class HTMLNode:
    def __init__(
        self,
        tag: str_or_none = None,
        value: str_or_none = None,
        children: list[HTMLNode] | None = None,
        props: dict[str, str]| None = None,
    ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self) -> str:
        if not self.props:
            return ""
        return " " + " ".join([f'{k}="{v}"' for k,v in self.props.items()])

    def __repr__(self) -> str:
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
