Challenge name: Bat Kube

Category: misc

Points: 94

Solves: 76


### Given information

> Unlucky, the flag is in Kubernetes and im not joking :/

> nc k8s.0xf.eu 8888

### Solution

Upon `netcat`-ing to the given host we receive a YAML response which is in fact a Kubernetes config:

```
Creating Cluster
Waiting for control plane............................................
Here is your Kubeconfig:

apiVersion: v1
clusters:
- cluster:
    server: https://flux-cluster-c92f12b8c63a464590e418baff193e78.0xf.eu
  name: ctf-cluster
contexts:
- context:
    cluster: ctf-cluster
    user: ctf-player
  name: ctf-cluster
[...]
users:
- name: ctf-player
  user:
    token: ey[...]mdQ

Leave this open until you solved the challenge, otherwise your cluster will be deleted. Please save it to a file and use it with kubectl --kubeconfig or use the KUBECONFIG env.
```

The obtained token appears to be an API key sort of thing assigned to the user `ctf-player`. Visiting the `server` url given in the response returns `403 Forbidden` with the note: anonymous access disallowed. We save token in a variable `token` for further use.

Let's begin the recon by listing all permissions granted to our token:
```
kubectl auth can-i --list --token=$token
```

```
deployments.*                                   []                                     []               [get list watch]
flags.*                                         []                                     []               [get list watch]
ingress.*                                       []                                     []               [get list watch]
namespaces.*                                    []                                     []               [get list watch]
pods.*                                          []                                     []               [get list watch]
services.*                                      []                                     []               [get list watch]
pods.*/log                                      []                                     []               [get]
```

---

After going through [this](https://ctftime.org/writeup/30561) writeup we proceed to list secrets, following which we obtain one secret named `kube-baby-flag-part1-of-3`, upon fetching which we get the fist part of the flag.

```
kubectl get secrets --token=$token
```

```
kubectl get secret kube-baby-flag-part1-of-3 -o jsonpath="{.data} --token=$token"
```

Returns `{"flag":"ZmxhZ3trOHNfMXNf","hint":"RG8geW91IGtub3cgbmFtZXNwYWNlcz8="}`

The given hint on `base64` decoding says "Do you know namespaces?"
Flag decodes to `flag{k8s_1s_`

The command by itself wasn't returning anything useful until the output format was specified as JSON with `-o jsonpath="{.data}`.

---

Listing all namespaces returns one namespace named `secret-namespace`. Querying that namespace for pods returns two pods.

```
kubectl get namespaces --all-namespaces --token=$token
```

```
kubectl get pods --namespace secret-namespace --output=custom-columns="NAME:.metadata.name,IMAGE:.spec.containers[*].image" --token=$token
```

```
kube-baby-flag-part2-of-3-6b97f47974-8vfbj   nginx
kube-baby-flag-part2-of-3-6b97f47974-cgxst   nginx
```

Reading the logs of one of the pods gives us the second part of the flag.

```
kubectl logs pod kube-baby-flag-part2-of-3-6b97f47974-cgxst
```

```
r34lly_fun_but
What about Flags in the Kubernetes API?
[...]
```

---

We proceed to save the namespace for convenience and then look for Kubernetes Flags.

```
kubectl config set-context --current --namespace=secret-namespace
```

Pro-tip: Append `-A` / `--all-namespaces` to `kubectl` command to query all namespaces at once.

```
kubectl get flags
```

Returns one Kubernetes flag. Trying to output it as JSON returns nothing but changing the output format to YAML gets us the last part of the flag.

```
kube-baby-flag-part3-of-3   You are on the right track, look more in detail!
```

```
kubectl get flag kube-baby-flag-part3-of-3 -o jsonpath="{.data}" # No output
```

```
kubectl get flag kube-baby-flag-part3-of-3 -o yaml
```

```
apiVersion: ctf.fluxfingers.hack.lu/v1
kind: Flag
metadata:
  creationTimestamp: "2023-10-15T16:56:11Z"
  name: kube-baby-flag-part3-of-3
  namespace: secret-namespace
  [...]
spec:
  flag: XzF0c18zdjNuX2IzdHQzcl8xbl9DVEZTfQ==
  hint: You are on the right track, look more in detail!
```

`flag{k8s_1s_r34lly_fun_but_1ts_3v3n_b3tt3r_1n_CTFS}`

---

### References

https://kubernetes.io/docs/reference/kubectl/

https://kubernetes.io/docs/reference/kubectl/cheatsheet/
