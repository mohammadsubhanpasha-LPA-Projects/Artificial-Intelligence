package knight.gareth

violation[msg] {
    input.request.kind.kind == "ServiceAccount"
    not input.request.object.metadata.annotations["spiffe.io/spiffe-id"]
    msg = "Must have SPIFFE ID annotation"
}
