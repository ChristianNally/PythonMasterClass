from torch import nn, save, load
from PIL import Image
from torch.optim import Adam
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor

train = datasets.MNIST(root="data", download=True, train=True, transform=ToTensor())
dataset = DataLoader(train, 32) # convert it to batches of 32 images

# create the neural network class
class ImageClassifier(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Conv2d(1, 32, (3,3)),
            nn.ReLU(),
            nn.Conv2d(32, 64, (3,3)),
            nn.ReLU(),
            nn.Conv2d(64, 64, (3,3)),
            nn.ReLU(),
            nn.Flatten(),
            nn.Linear(64*(28-6)*(28-6), 10)
        )

    def forward(self, x): # like the call method in TensorFlow
        return self.model(x)

# Instance of the neural network, less, optimizer
clf = ImageClassifier().to('cpu')
opt = Adam(clf.parameters(), lr=1e-3)
loss_fn = nn.CrossEntropyLoss()

#    Training flow
if __name__ == "__main__":

    if True:
            with open('model_state.pt', 'rb') as f:
                clf.load_state_dict(load(f))
                img = Image.open('image_1.jpg')
                img_tensor = img.ToTensor()(img).unsqueeze(0)
                print(clf(img_tensor))
    else:
        for epoch in range(10): # train for 10 epochs
            for batch in dataset:
                X,y = batch
                X, y = X.to('cpu'), y.to('cpu')
                yhat = clf(X)
                loss = loss_fn(yhat, y)

                # Apply backprop
                opt.zero_grad()
                loss.backward()
                opt.step()

                print(f"Epoch: {epoch} loss is {loss.item()}")

        with open('model_state.pt', 'wb') as f:
            save(clf.state_dict(), f)
