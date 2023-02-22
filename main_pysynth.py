import pysynth as ps
test = (('f', 4), ('e5*', 8), ('f', -4),
  ('c', 4), ('c', 4), ('g6', 4),
  ('g*', 2), ('g', 4),
  ('r', 4))
ps.make_wav(test, fn = "test.wav")