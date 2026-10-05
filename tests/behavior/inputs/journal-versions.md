# Constructed version comparison

Conference v1, Section 3: When a cached entry's epoch differs from the worker epoch, invalidate it before reuse.

Journal v2, Section 3: When a cached entry's epoch differs from the worker epoch, invalidate it before reuse. For example, entry epoch 4 cannot be reused by worker epoch 5. This prevents reuse across a restart.

Journal v2, contributions: We introduce a new epoch invalidation mechanism absent from the conference version.

No code change or new experiment accompanies these passages. Both are original fictional texts under Apache-2.0.
